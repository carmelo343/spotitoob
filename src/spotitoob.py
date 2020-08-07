import youtube_client
import spotify_client


def main():
    # YOUTUBE
    youtube = youtube_client.YoutubeClient()
    youtube_playlist_id = 'PL0m_RB_7CwlAU66D3XDZpVquBgt7psmoi'
    youtube_songs = youtube.get_songs(youtube_playlist_id)

    if(youtube_songs != None):
        print("Songs in youtube playlist:")
        for song in youtube_songs:
            print(f"{song.track} {song.artist}")
    else:
        print("Unable to retreive song info from youtube")



    # SPOTIFY
    spotify = spotify_client.SpotifyClient()
    song_ids = spotify.get_song_ids(youtube_songs)

    for song_id in song_ids:
        print(song_id)

if __name__ == "__main__":
    main()