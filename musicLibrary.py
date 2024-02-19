music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': ['Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': ['Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

while True:
    print("\nCommands:")
    print("1. Add Artist")
    print("2. Add Album")
    print("3. Add Song")
    print("Type 'exit' to quit.")

    choice = input("Enter your choice: ")

    if choice == 'exit':
        break
    elif choice == '1':
        artist_name = input("Enter the artist name: ")
        if artist_name not in music:
            music[artist_name] = {}
            print("Artist added successfully.")
        else:
            print("Artist already exists in the library.")
    elif choice == '2':
        artist_name = input("Enter the artist name: ")
        if artist_name in music:
            album_name = input("Enter the album name: ")
            if album_name not in music[artist_name]:
                year = input("Enter the year of the album: ")
                platinum = input("Is the album platinum? (True/False): ").capitalize() == 'True'
                music[artist_name][album_name] = {'songs': [], 'year': year, 'platinum': platinum}
                print("Album added successfully.")
            else:
                print("Album already exists for this artist.")
        else:
            print("Artist not found in the library.")
    elif choice == '3':
        artist_name = input("Enter the artist name: ")
        if artist_name in music:
            album_name = input("Enter the album name: ")
            if album_name in music[artist_name]:
                song_name = input("Enter the song name: ")
                music[artist_name][album_name]['songs'].append(song_name)
                print("Song added successfully.")
            else:
                print("Album not found for this artist.")
        else:
            print("Artist not found in the library.")
    else:
        print("Invalid choice. Please try again.")
