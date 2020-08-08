import requests
import urllib.parse
import os


class SpotifyClient:
    def __init__(self):
        self.user_id = os.getenv("SPOTIFY_USER_ID")
        self.auth_token = RefreshToken().get_token()
    
    def get_songs_in_playlist(self, playlist_id):
        query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

        response = requests.get(query,
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
                }
            )

        response_json = response.json()
        return response_json

    def get_song_uris(self, songs):
        song_uris = []
        for song in songs:
            query = urllib.parse.quote(f"{song.track} {song.artist}")
            url = f"https://api.spotify.com/v1/search?q={query}&type=track"
            response = requests.get(url, 
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.auth_token}"
                }
            )
            reponse_json = response.json()
            song_uri = reponse_json['tracks']['items'][0]['uri']
            song_uris.append(song_uri)

        return song_uris

    def add_to_playlist(self, playlist_id, song_uris):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris="
        uris = ','.join(song_uris)
        url += uris

        response = requests.post(url, 
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.auth_token}"
                }
            )
            
        reponse_json = response.json()



# Spotify authorization tokens expire after 1hr
class RefreshToken:
    def __init__(self):
        self.refresh_token = os.getenv('SPOTIFY_REFRESH_TOKEN')
        self.client_id_secret_b64 = os.getenv('SPOTIFY_CLIENT_ID_SECRET_B64')

    def get_token(self):
        query = "https://accounts.spotify.com/api/token"
        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": self.refresh_token},
                                 headers={"Authorization": f"Basic {self.client_id_secret_b64}"})

        response_json = response.json()
        return response_json["access_token"]