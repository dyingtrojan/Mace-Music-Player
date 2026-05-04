from tinytag import TinyTag, Image

def get_song_info(song_path):
    file = song_path
    tags: TinyTag = TinyTag.get(song_path, image=True)
    return tags