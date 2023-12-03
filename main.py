import argparse
import random

from authorization import *
from commonality import calculate_user_familiarity_for_g, calculate_commonality_for_g
from rankings import editorial_categories, generate_p_users
from datalist import *
from playlist import *

client_id = ""
client_secret = ""
init_artist_id = "32iu6edxEe5fMPX029eAU3"


def users(n, m):
    return generate_p_users(n, m)


def metric_calculations(p, user_list):
    familiarities = []
    commonalities = []

    for g in editorial_categories:
        fg = []
        for pu in user_list:
            familiarity = calculate_user_familiarity_for_g(pu, g, p)
            fg.append(familiarity)
        familiarities.append(fg)

    for f in familiarities:
        commonality = calculate_commonality_for_g(f)
        commonalities.append(commonality)
    print("Commonalities", commonalities)


#     parser.add_argument("-m", "--Users", help="Amount of Users to generate")
#     parser.add_argument("-n", "--List", help="Size of rank list to generate")
#     parser.add_argument("-p", "--Patience", help="User's patience to use at the RBP")
#     ul = users(int(args.Users), int(args.List))
#     pprint(ul)
#     metric_calculations(float(args.Patience), ul)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-ci", "--ClientId", help="Client Id of the Spotify Application")
    parser.add_argument("-cs", "--ClientSecret", help="Client Secret of the Spotify Application")
    # Read arguments from command line
    args = parser.parse_args()

    client_id = args.ClientId
    client_secret = args.ClientSecret

    session = create_spotify_session(client_id)
    get_user_authorization(session)
    # Get the authorization verifier code from the callback url
    redirect_response = input('\n\nPaste the full redirect URL here: ')
    token = get_token(session, redirect_response, client_id, client_secret)

    # Get current user
    # current_user_id = get_user_info(token["access_token"])

    # create_playlist(token["access_token"], current_user_id)
    # get_and_categorize_data(token["access_token"])

    main_artists = read_data_pop_artists_files()
    main_artists = choose_artists_for_list(main_artists, 0.5, 20)
    main_items = get_all_tops(main_artists, token["access_token"])

    special_unpop = read_data_unpop_artists_files()
    special_unpop = choose_artists_for_list(special_unpop, 0.5, 5)
    special_unpop_items = get_all_tops(special_unpop, token["access_token"])

    special_female_unpop = read_data_pop_female_artists_files()
    special_female_unpop = choose_artists_for_list(special_female_unpop, 0.5, 5)
    special_female_unpop_items = get_all_tops(special_female_unpop, token["access_token"])

    the_list = create_playlist_items(main_items, special_unpop_items, special_female_unpop_items)
    add_items_to_playlist(the_list, token["access_token"])
