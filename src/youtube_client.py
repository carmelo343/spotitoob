from googleapiclient.discovery import build
import youtube_dl
import os


class Song:
  def __init__(self, title, artist):
    self.title = title
    self.artist = artist

class YoutubeClient:
    def __init__(self):
        #set a custom agent (use facebook's web crawler)
        youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
        self.youtube_client = build('youtube', 'v3', developerKey=os.getenv("YOUTUBE_API_KEY"))

    def _get_video_ids(self, playlist_id):
        video_ids = []
        request = self.youtube_client.playlistItems().list(
            part="snippet",
            maxResults=50,
            playlistId=playlist_id
        )
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['snippet']['resourceId']['videoId'])

        return video_ids

    def get_songs(self, playlist_id):
        video_ids = self._get_video_ids(playlist_id)
        songs = []
        base_url = "https://youtube.com/watch?v="
        for video_id in video_ids:
            video_url = base_url + video_id
            video_info = youtube_dl.YoutubeDL({}).extract_info(video_url, download = False)

            songs.append(
                Song(video_info['track'], video_info['artist'])
            )
        
        return songs