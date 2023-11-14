import requests

playlist_url = "https://api.spotify.com/v1/users/anastasia_protopapa/playlists"

playlist_info = {
    "name": "A Playlist adhering to the Commonality ",
    "description": "A Playlist that satisfies a certain metric",
    "public": True
}


def create_playlist(access_token):
    headers = {'Authorization': "Bearer " + access_token, 'Content-Type': 'application/json'}
    response = requests.post(playlist_url, headers=headers, json=playlist_info)
    attributes = vars(response)
    for attribute, value in attributes.items():
        print(attribute, "=", value)
