import os

user = os.environ['USERPROFILE']
musicPath = os.path.join(user, r'Music\Songs')
songsList = os.listdir(musicPath)
