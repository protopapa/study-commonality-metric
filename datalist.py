import json
import operator

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
