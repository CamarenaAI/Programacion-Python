def make_album(artist_name, album_title, tracks=''):
    album = {'artist': artist_name, 'album': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nPlease tell album name:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break

    n_tracks = input("Num. tracks: ")
    if a_title == 'q':
        break

    album_name = make_album(a_name, a_title)
    print(album_name)