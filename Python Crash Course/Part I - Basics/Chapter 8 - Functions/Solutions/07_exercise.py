def make_album(artist_name, album_title, tracks=''):
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

music_album = make_album('michael jackson', 'thriller', tracks=9)
print(music_album)

music_album = make_album('eminem', 'kamikaze')
print(music_album)

music_album = make_album('likin park', 'meteora')
print(music_album)