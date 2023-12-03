from pprint import pprint

import requests

base_url = "https://api.spotify.com/v1/"
artists = "artists/"
related_artists = "/related-artists"
tracks = "/top-tracks"
init_artist_id = "32iu6edxEe5fMPX029eAU3"


def get_artist(artist_id, access_token):
    headers = {'Authorization': "Bearer " + access_token}
    response = requests.get(base_url + artists + artist_id, headers=headers)
    return response.json()


def get_similar_artists(artist_id, access_token):
    headers = {'Authorization': "Bearer " + access_token}
    response = requests.get(base_url + artists + artist_id + related_artists, headers=headers)
    s_artists = response.json()
    return s_artists.get('artists')


def get_init_artist(access_token):
    headers = {'Authorization': "Bearer " + access_token}
    response = requests.get(base_url + artists + init_artist_id, headers=headers)
    artist = response.json()
    return artist


def get_artist_tree(access_token):
    artists_list = []
    artists_id_list = []
    temp_sar_list = []

    i_artist = get_init_artist(access_token)
    artists_list.append(i_artist)
    artists_id_list.append(i_artist.get('id'))
    temp_sar_list.append(i_artist)

    while len(artists_list) < 200:
        for ar in temp_sar_list:
            sa = get_similar_artists(ar.get('id'), access_token)
            for sar in sa:
                if sar.get('id') not in artists_id_list:
                    artists_list.append(sar)
                    artists_id_list.append(sar.get('id'))
            temp_sar_list = sa
    return artists_list


def get_all_tops(alist, access_token):
    mt = []
    for a in alist:
        mt = mt + get_artists_top(a, access_token)

    return mt


def get_artists_top(a, access_token):
    param = {"market": "GR"}
    headers = {'Authorization': "Bearer " + access_token}
    response = requests.get(base_url + artists + a.get("id") + tracks, headers=headers, params=param)
    t = response.json()
    return t.get('tracks')
