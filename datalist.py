import ast
import json
import operator
import random

from artists import *


def get_and_categorize_data(access_token):
    artists_list = get_artist_tree(access_token)
    artists_list = sorted(artists_list, key=operator.itemgetter('popularity'))

    popular = []
    not_that_popular = []
    for artist in artists_list:
        if artist.get('popularity') < 30:
            not_that_popular.append(artist)
        else:
            popular.append(artist)

    print("Popular artists are: ", len(popular))
    print("Un-Popular artists are: ", len(not_that_popular))

    with open('unpop-artists.json', 'w') as convert_file:
        convert_file.write(json.dumps(not_that_popular))

    with open('pop-artists.json', 'w') as convert_file:
        convert_file.write(json.dumps(popular))

    female_unpop_art = []
    for art in not_that_popular:
        print("Artist : ", art.get('name'))
        print("\n")
        answer = input('\n\nIs this artist female or male ? f/m')
        if answer == "f":
            female_unpop_art.append(art)

    print("Female Un-Popular artists are: ", len(female_unpop_art))

    with open('female-unpop-artists.json', 'w') as convert_file:
        convert_file.write(json.dumps(female_unpop_art))


def choose_artists_for_list(al, threshold, size):
    random.shuffle(al)
    chosen_artists = []
    for a in al:
        if len(chosen_artists) >= size:
            break
        if random.uniform(0, 1) > threshold:
            if a.get("popularity") > 4:
                chosen_artists.append(a)

    return chosen_artists


def read_data_artists_files():
    with open('artists.json', encoding='utf-8') as json_file:
        data = json.load(json_file)

    return data


def read_data_unpop_artists_files():
    with open('unpop-artists.json', encoding='utf-8') as json_file:
        unpop = json.load(json_file)

    return unpop


def read_data_pop_artists_files():
    with open('pop-artists.json', encoding='utf-8') as json_file:
        pop = json.load(json_file)

    return pop


def read_data_pop_female_artists_files():
    with open('female-unpop-artists.json', encoding='utf-8') as json_file:
        f = json.load(json_file)

    return f
