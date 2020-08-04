import youtube_client
import os


def main():
    youtube = youtube_client.YoutubeClient(os.getenv('YOUTUBE_API_KEY'))
    
    playlist_id = 'PL0m_RB_7CwlAU66D3XDZpVquBgt7psmoi'
    songs = youtube.get_songs(playlist_id)

    if(songs != None):
        for song in songs:
            print(f"{song.title} {song.artist}")
    else:
        print("Unable to retreive song info")


if __name__ == "__main__":
    main()