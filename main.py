from pprint import pprint

from commonality import calculate_user_recall_for_g_in_k, calculate_rank_biased_precision, \
    calculate_user_familiarity_for_g, calculate_commonality_for_g
from rankings import generate_p_user, editorial_categories, generate_p_users

user_patience = 0.8

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    users = generate_p_users(30, 3000)

    familiarities = []
    for pu in users:
        familiarity = calculate_user_familiarity_for_g(pu, editorial_categories[0], user_patience)
        familiarities.append(familiarity)

    pprint(familiarities)

    commonality = calculate_commonality_for_g(familiarities)
    print(f"Commonality", commonality)
