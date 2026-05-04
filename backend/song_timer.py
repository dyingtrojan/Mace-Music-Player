from backend import song_mixer
import threading

time = 0.0
def atualizar_tempo():
    while True:
        time = song_mixer.get_song_time()
    
thread_timer = threading.Thread(target=atualizar_tempo, daemon=True)
thread_timer.start()