import os
import re
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3


def do_it():
    directory = 'D:\Muzica\\'
    for file_name in os.listdir(directory):
        old_file_name = str(directory) + str(file_name)
        if old_file_name.endswith('.flac'):
            song = FLAC(old_file_name)
            new_file_name = directory + strip_song(song) + ".flac"
            os.rename(old_file_name, new_file_name)
        else:
            song = EasyID3(old_file_name)
            new_file_name = directory + strip_song(song) + ".mp3"
            os.rename(old_file_name, new_file_name)


def strip_song(song):

    """
    Strip illegal characters from the file name
    """
    if 'artist' in song:
        artist = str(song['artist'])
    else:
        artist = ''
    if 'title' in song:
        title = str(song['title'])
    else:
        title = ''
    if (artist.startswith("['") and artist.endswith("']")) or (artist.startswith("[\"") and artist.endswith("\"]")):
        artist = artist[2:-2]
    if (title.startswith("['") and title.endswith("']")) or (title.startswith("[\"") and title.endswith("\"]")):
        title = title[2:-2]
    new_file_name = str(artist) + " - " + str(title)
    new_file_name = re.sub('[\\\/:*?"<>|]', '', new_file_name)
    return new_file_name