import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from backend import song_mixer, queue_manager, metadata_manager
import io
import os

directory = ''
songs = []
songsLabel = []
song_index = 0

app = ctk.CTk()
app.geometry("1000x600")
app.title("Mace Music Player")

app.grid_columnconfigure(0, weight=1)


songList = ctk.CTkScrollableFrame(app, fg_color="#1f1f1f")
songList.grid(column=0, sticky="nesw", rowspan=100)

def choose_dir():
    directory = filedialog.askdirectory(title="Choose a directory with your audio files.")
    songsLabel = []
    print(f"directory chosen: {directory}")
    directory_stuff = os.listdir(directory)
    interation = 0
    for file in directory_stuff:
        if file[-4:] == ".wav":
            interation += 1
            print(f"Arquivo permitido: {file}")
            
            songsLabel.append(ctk.CTkButton(songList, text=file, command= lambda file_name=file: start_song(fr"{directory}/{file_name}")))
            queue_manager.queue.append(fr"{directory}/{file}")
            songs.append(file)
        else:
            print(f"O arquivo {file} não é um arquivo de audio valido.")
    for i in songsLabel:
        i.grid(row=interation, column=0, pady=20, padx=20)
        interation += 1
    start_song(queue_manager.queue[0])
    queue_manager.index_song = 0

menuBar = tk.Menu(app)
app.config(menu=menuBar)

music_dir = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=music_dir)
music_dir.add_command(label="Open", command=choose_dir)


playBtn_icon = ctk.CTkImage(Image.open("assets/play.png"), size=(16,16))

albumCoverImage = ctk.CTkImage(Image.open("assets/no-cover.png"),size=(150,150))

albumCoverLabel = ctk.CTkLabel(app, text="", image=albumCoverImage)
albumCoverLabel.grid(row=0, column=1, pady=20, padx=20)

songTitleLabel = ctk.CTkLabel(app, text="Artist Name - Song Name")
songTitleLabel.grid(row=1, column=1, pady=20, padx=20)

albumTitleLabel = ctk.CTkLabel(app, text="Album Name")
albumTitleLabel.grid(row=2, column=1, pady=20, padx=20)

time_slider = ctk.CTkSlider(app, width=500)
time_slider.grid(row=4, column=1)

def next_song():
    queue_manager.next_song()
    change_ui_song(queue_manager.queue[queue_manager.index_song])

def last_song():
    queue_manager.last_song()
    change_ui_song(queue_manager.queue[queue_manager.index_song])
    
def change_ui_song(song):
    tags = metadata_manager.get_song_info(song)
    
    songTitleLabel.configure(app, text=f"{tags.artist} - {tags.title}")
    albumTitleLabel.configure(app, text=f"{tags.album}")
    albumCover = Image.open(io.BytesIO(tags.images.front_cover.data))
    albumCoverCtk = ctk.CTkImage(albumCover, albumCover, size=(150,150))
    albumCoverLabel.configure(app, text="", image=albumCoverCtk)
    time_slider.configure(app, from_=0, to=song_mixer.get_song_length(), variable=slider_time, command=song_mixer.change_time)
    change_slider()
slider_time = ctk.DoubleVar(value=song_mixer.get_song_time())

def change_slider():
    slider_time.set(song_mixer.get_song_time())
    app.after(500, change_slider)

def start_song(song_file):
    
    song_mixer.play_song(song_file)
    queue_manager.index_song = queue_manager.queue.index(song_file)
    change_ui_song(song_file)

buttons_frame = ctk.CTkFrame(app, fg_color="transparent")
buttons_frame.grid(row=3, column=1, pady=20, padx=20)

back_btn = ctk.CTkButton(buttons_frame, text="Back", command=lambda: last_song())
back_btn.grid(row=0, column=0, pady=20, padx=20)

play_btn = ctk.CTkButton(buttons_frame, text="", image=playBtn_icon, command=lambda: song_mixer.pause_song())
play_btn.grid(row=0, column=1, pady=20, padx=20)

next_btn = ctk.CTkButton(buttons_frame, text="Next", command=lambda: next_song())
next_btn.grid(row=0, column=2, pady=20, padx=20)

change_slider()

app.mainloop()
