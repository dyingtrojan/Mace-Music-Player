import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from backend import song_mixer
import io
import os

directory = ''
songs = []
songsLabel = []

app = ctk.CTk()
app.geometry("1000x600")
app.title("Mace Music Player")

app.grid_columnconfigure(0, weight=1)


songList = ctk.CTkScrollableFrame(app, fg_color="#1f1f1f")
songList.grid(column=0, sticky="nesw", rowspan=50)

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
            
            songsLabel.append(ctk.CTkButton(songList, text=file, command= lambda file_name=file: play_song(fr"{directory}/{file_name}")))
            song_mixer.queue.append(fr"{directory}/{file}")
            songs.append(file)
        else:
            print(f"O arquivo {file} não é um arquivo de audio valido.")
    for i in songsLabel:
        i.grid(row=interation, column=0, pady=20, padx=20)
        interation += 1
    song_mixer.load_queue()
    

menuBar = tk.Menu(app)
app.config(menu=menuBar)

music_dir = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=music_dir)
music_dir.add_command(label="Open", command=choose_dir)


albumCoverImage = ctk.CTkImage(Image.open("assets/no-cover.png"),size=(150,150))

albumCoverLabel = ctk.CTkLabel(app, text="", image=albumCoverImage)
albumCoverLabel.grid(row=0, column=1, pady=20, padx=20)

songTitleLabel = ctk.CTkLabel(app, text="Artist Name - Song Name")
songTitleLabel.grid(row=1, column=1, pady=20, padx=20)

albumTitleLabel = ctk.CTkLabel(app, text="Album Name")
albumTitleLabel.grid(row=2, column=1, pady=20, padx=20)


def play_song(song_file):
    song_mixer.play_song(song_file)
    tags = song_mixer.get_song_info(song_file)
    
    songTitleLabel.configure(app, text=f"{tags.artist} - {tags.title}")
    albumTitleLabel.configure(app, text=f"{tags.album}")
    albumCover = Image.open(io.BytesIO(tags.images.front_cover.data))
    albumCoverCtk = ctk.CTkImage(albumCover, albumCover, size=(150,150))
    
    albumCoverLabel.configure(app, text="", image=albumCoverCtk)
    

buttons_frame = ctk.CTkFrame(app, fg_color="transparent")
buttons_frame.grid(row=3, column=1, pady=20, padx=20)

back_btn = ctk.CTkButton(buttons_frame, text="Back")
back_btn.grid(row=0, column=0, pady=20, padx=20)

play_btn = ctk.CTkButton(buttons_frame, text="Play", command=lambda: song_mixer.load_queue())
play_btn.grid(row=0, column=1, pady=20, padx=20)

next_btn = ctk.CTkButton(buttons_frame, text="Next")
next_btn.grid(row=0, column=2, pady=20, padx=20)

app.mainloop()
