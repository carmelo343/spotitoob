from googleapiclient.discovery import build
import os

apiKey = os.environ['API_KEY']
youtube = build('youtube', 'v3', developerKey=apiKey)

def main():
    print("Enter playlist id: ")
    playlistId = input()

    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=100,
        playlistId=playlistId
    )
    response = request.execute()

    print(response)


if __name__ == "__main__":
    main()