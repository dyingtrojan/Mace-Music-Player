import customtkinter as ctk
from PIL import Image
app = ctk.CTk()
app.geometry("1000x600")
app.title("Mace Music Player")

app.grid_columnconfigure(0, weight=1)

albumCovCTkImage = ctk.CTkImage(Image.open("assets test/mozart masterpieces.png"), size=(150,150))

albumCovLabel = ctk.CTkLabel(app, image=albumCovCTkImage, text="")
albumCovLabel.grid(row=0, column=0, pady=20, padx=20)

songTitleLabel = ctk.CTkLabel(app, text="Artist Name - Song Name")
songTitleLabel.grid(row=1, column=0, pady=20, padx=20)

albumTitleLabel = ctk.CTkLabel(app, text="Album Name")
albumTitleLabel.grid(row=2, column=0, pady=20, padx=20)

buttons_frame = ctk.CTkFrame(app, fg_color="transparent")
buttons_frame.grid(row=3, column=0, pady=20, padx=20)

back_btn = ctk.CTkButton(buttons_frame, text="Back")
back_btn.grid(row=0, column=0, pady=20, padx=20)

play_btn = ctk.CTkButton(buttons_frame, text="Play")
play_btn.grid(row=0, column=1, pady=20, padx=20)

next_btn = ctk.CTkButton(buttons_frame, text="Next")
next_btn.grid(row=0, column=2, pady=20, padx=20)

app.mainloop()