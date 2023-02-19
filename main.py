from pprint import pprint

import numpy as np

from commonality import calculate_user_recall_for_g_in_k
from rankings import generate_p_user, editorial_categories

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pu = generate_p_user()
    np.random.shuffle(pu)

    recall = calculate_user_recall_for_g_in_k(pu, editorial_categories[0], 10)
    # familiarity = calculate_familiarity_u_g(pu, editorial_categories[0])
    # print(f"familiarity", familiarity)
