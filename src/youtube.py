from googleapiclient.discovery import build
import os

apiKey = os.environ['API_KEY']
youtube = build('youtube', 'v3', developerKey=apiKey)

def getSongList(playlistId):
    songList = []
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=50,
        playlistId=playlistId
    )
    response = request.execute()

    for item in response['items']:
        songList.append(item['snippet']['title'])

    return songList