import pygame
from PIL import Image
import wave
from backend import queue_manager
import datetime


pygame.mixer.pre_init(48000, -16, 2, 512)
pygame.mixer.init()

old_pos_song = 0

playing_now = ""

is_paused = True

def get_pygame_busy_state():
    return pygame.mixer.music.get_busy()

def convert_seconds_to_minutes(value):
    return f"{datetime.timedelta(seconds=round(value))}"

def play_song(song_path):
    global is_paused
    is_paused = False
    global playing_now, old_pos_song
    old_pos_song = 0
    playing_now = song_path
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(0, 0.0)

def get_song_time():
    return (pygame.mixer.music.get_pos() + (old_pos_song * 1000)) / 1000

def pause_song():
    global is_paused
    if is_paused == True:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.pause()
        is_paused = True
def change_time(value):
    global old_pos_song
    old_pos_song = value
    if playing_now[-4:] == ".wav":
        pygame.mixer.music.stop()
        pygame.mixer.music.play(0, value)

def get_song_length():
    duration = 0.0
    try:
        with wave.open(playing_now, "rb") as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = (frames / float(rate))
    except Exception as e:
        print("Deu erro aqui.")
    return duration