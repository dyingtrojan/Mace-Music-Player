import pygame
from tinytag import TinyTag, Image
from PIL import Image

pygame.mixer.pre_init(48000, -16, 2, 512)
pygame.mixer.init()

queue = []

def load_queue():
    pygame.mixer.music.load(queue[0])
    pygame.mixer.music.play(0, 0.0)
    interation = 0
    for i in queue:
        if interation == 0:
            interation += 1
        else:
            pygame.mixer.music.queue(i)
        interation += 1

def play_song(song_path):
    if pygame.mixer.get_busy:
        pygame.mixer.music.stop()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(0, 0.0)

def get_song_info(song_path):
    file = song_path
    tags: TinyTag = TinyTag.get(song_path, image=True)
    return tags

