from backend import song_mixer
import pygame

queue = []
pygame.mixer.pre_init(48000, -16, 2, 512)
pygame.mixer.init()

index_song = 0

def next_song():
    global index_song
    index_song += 1
    song_mixer.play_song(queue[index_song])
    
def last_song():
    global index_song
    index_song -= 1
    song_mixer.play_song(queue[index_song])