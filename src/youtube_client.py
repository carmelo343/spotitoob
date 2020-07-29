from googleapiclient.discovery import build
import youtube_dl


class Song:
  def __init__(self, title, artist):
    self.title = title
    self.artist = artist

class YoutubeClient:
    def __init__(self, api_key):
        self.youtube_client = build('youtube', 'v3', developerKey=api_key)

    def get_videoid_list(self, playlist_id):
        videoid_list = []
        request = self.youtube_client.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=playlist_id
        )
        response = request.execute()

        for item in response['items']:
            videoid_list.append(item['snippet']['resourceId']['videoId'])

        return videoid_list

    def get_song_list(self, video_id_list):
        song_list = []
        base_url = "https://youtube.com/watch?v="
        for video_id in video_id_list:
            video_url = base_url + video_id
            video_info = youtube_dl.YoutubeDL({}).extract_info(video_url, download = False)

            song_list.append(
                Song(video_info['track'], video_info['artist'])
            )