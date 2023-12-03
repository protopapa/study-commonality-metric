import requests

base_url = "https://api.spotify.com/v1/users/"
playlists = "/playlists"

playlist_info = {
    "name": "A Playlist adhering to the Commonality ",
    "description": "A Playlist that satisfies a certain metric",
    "public": True
}


def create_playlist(access_token, user_id):
    headers = {'Authorization': "Bearer " + access_token, 'Content-Type': 'application/json'}
    response = requests.post(base_url + user_id + playlists, headers=headers, json=playlist_info)
    return response.status_code


def create_playlist_items(main_list, unpop_list, female_list):
    return 0
