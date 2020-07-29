import youtube_client
import os


def main():
    youtube = youtube_client.YoutubeClient(os.getenv('YOUTUBE_API_KEY'))
    
    videoid_list = youtube.get_videoid_list('PL0m_RB_7CwlAU66D3XDZpVquBgt7psmoi')
    song_list = youtube.get_song_list(videoid_list)

    if(song_list != None):
        for song in song_list:
            print(f"{song.title} - {song.artist}")
    else:
        print("Unable to retreive song info")


if __name__ == "__main__":
    main()