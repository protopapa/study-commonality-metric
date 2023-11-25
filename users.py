import requests

base_url = "https://api.spotify.com/v1/me"
top_items = "/top/tracks"
myself = "me"


def get_user_info(access_token):
    headers = {'Authorization': "Bearer " + access_token}
    me = requests.get(base_url, headers=headers)
    return me.json()["id"]


def get_user_top_tracks(access_token):
    headers = {'Authorization': "Bearer " + access_token}
    response = requests.get(base_url + top_items, headers=headers)
    return response.status_code
