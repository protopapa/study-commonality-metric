import random
from pprint import pprint

import requests

playlist_id = "6UbODPOzRQxLPOH5pt4NCB"
base_url = "https://api.spotify.com/v1/playlists/"
base_user_url = "https://api.spotify.com/v1/users/"
playlists = "/playlists"
tracks = "/tracks"

playlist_info = {
    "name": "A Playlist adhering to the Commonality ",
    "description": "A Playlist that satisfies a certain metric",
    "public": True
}


def create_playlist(access_token, user_id):
    headers = {'Authorization': "Bearer " + access_token, 'Content-Type': 'application/json'}
    response = requests.post(base_user_url + user_id + playlists, headers=headers, json=playlist_info)
    return response.status_code


def add_items_to_playlist(the_list, access_token):
    uris = get_uris(the_list)
    track_info = {
        "uris": uris,
        "position": 0
    }

    headers = {'Authorization': "Bearer " + access_token, 'Content-Type': 'application/json'}
    response = requests.post(base_url + playlist_id + tracks, headers=headers, json=track_info)
    pprint(response.json())
    return response.status_code


def get_uris(the_list):
    uris = []
    for item in the_list:
        uris.append(item.get('uri'))

    return uris


def create_playlist_items(main_list, unpop_list, female_list):
    final_list = []
    ideal_List = []

    for i in unpop_list:
        if random.uniform(0, 1) > 0.5:
            if len(ideal_List) >= 25:
                break
            else:
                ideal_List.append(i)

    for f in female_list:
        if random.uniform(0, 1) > 0.5:
            if len(ideal_List) >= 50:
                break
            else:
                ideal_List.append(f)

    for item in ideal_List:
        if len(final_list) >= 100:
            break
        if random.uniform(0, 1) > 0.5:
            final_list.append(item)
        else:
            final_list.append(random.choice(main_list))

    return final_list
