from pprint import pprint

from commonality import calculate_recall, calculate_familiarity_u_g
from rankings import build_user_p, editorial_categories

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pu = build_user_p()
    # recall = calculate_recall(pu, editorial_categories[0], 10)
    familiarity = calculate_familiarity_u_g(pu, editorial_categories[0])

    print(f"familiarity", familiarity)
