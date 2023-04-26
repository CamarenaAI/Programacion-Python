"""
8.8 User Album

Start with your program from Exercise 8.7. Write a while loop that
allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the
dictionary that’s created. Be sure to include a quit value in the while
loop
"""

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