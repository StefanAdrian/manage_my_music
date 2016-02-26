import os


def generate_playlist():
    """
    Outputs a .txt file that contains the names of my songs
    """

    with open(r'C:\Users\Adrian\Desktop\Muzica.txt', 'w+', encoding='utf-8') as playlist:
        playlist_songs = os.listdir('D:\Muzica\\')
        for song in playlist_songs:
            playlist.write(song + '\n')


