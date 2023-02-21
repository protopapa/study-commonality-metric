from commonality import calculate_user_familiarity_for_g, calculate_commonality_for_g
from rankings import editorial_categories, generate_p_users

user_patience = 0.8

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    users = generate_p_users(10, 3000)

    familiarities = []
    commonalities = []

    for g in editorial_categories:
        fg = []
        for pu in users:
            familiarity = calculate_user_familiarity_for_g(pu, g, user_patience)
            fg.append(familiarity)
        familiarities.append(fg)

    for f in familiarities:
        commonality = calculate_commonality_for_g(f)
        commonalities.append(commonality)
    print(f"Commonalities", commonalities)
