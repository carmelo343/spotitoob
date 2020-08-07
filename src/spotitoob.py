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
            print(f"{song.track} {song.artist}")
    else:
        print("Unable to retreive song info from youtube")



    # SPOTIFY
    spotify = spotify_client.SpotifyClient()

    song_result = spotify.search_song(songs[0].track, songs[0].artist)


if __name__ == "__main__":
    main()