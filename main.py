import argparse

from authorization import *
from commonality import calculate_user_familiarity_for_g, calculate_commonality_for_g
from rankings import editorial_categories, generate_p_users
from datalist import *

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
    print(f"Commonalities", commonalities)


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

    a_list = read_data_artists_files()
    ap_list = read_data_pop_artists_files()
    aupop_list = read_data_unpop_artists_files()
    afemale_list = read_data_pop_female_artists_files()
