import argparse
from pprint import pprint

from commonality import calculate_user_familiarity_for_g, calculate_commonality_for_g
from rankings import editorial_categories, generate_p_users


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-m", "--Users", help="Amount of Users to generate")
    parser.add_argument("-n", "--List", help="Size of rank list to generate")
    parser.add_argument("-p", "--Patience", help="User's patience to use at the RBP")
    # Read arguments from command line
    args = parser.parse_args()

    ul = users(int(args.Users), int(args.List))
    pprint(ul)

    metric_calculations(float(args.Patience), ul)
