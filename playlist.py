import requests

playlist_url = "https://api.spotify.com/v1/users/anastasia_protopapa/playlists"

playlist_info = {
    "name": "Commonality Playlist",
    "description": "New playlist description",
    "public": "false"
}


def create_playlist(access_token):
    headers = {'Authorization': "Bearer " + access_token, 'Content-Type': 'application/json'}
    response = requests.post(playlist_url, data=playlist_info, headers=headers)
    print(response)
