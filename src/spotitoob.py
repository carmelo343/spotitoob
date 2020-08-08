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
    spotify_playlist_id = "2DAjIdyfwslcmz1YHNH8u6"
    
    song_uris = spotify.get_song_uris(youtube_songs)
    for uri in song_uris:
        print(uri)

    spotify.add_to_playlist(spotify_playlist_id, song_uris)

if __name__ == "__main__":
    main()