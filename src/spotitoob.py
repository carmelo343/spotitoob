import youtube_client
import spotify_client


def main():
    # YOUTUBE
    youtube = youtube_client.YoutubeClient()
    youtube_playlist_id = 'PL0m_RB_7CwlAU66D3XDZpVquBgt7psmoi'
    songs = youtube.get_songs(youtube_playlist_id)

    if(songs != None):
        print("Songs in youtube playlist:")
        for song in songs:
            print(f"{song.title} {song.artist}")
    else:
        print("Unable to retreive song info from youtube")



    # SPOTIFY
    spotify = spotify_client.SpotifyClient()
    spotify_playlist_id = '37i9dQZF1E35hei03EgTqe'

    response_json = spotify.get_songs_in_playlist(spotify_playlist_id)
    print(response_json)


if __name__ == "__main__":
    main()