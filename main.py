from pprint import pprint

import numpy as np

from commonality import calculate_user_recall_for_g_in_k, calculate_rank_biased_precision, \
    calculate_user_familiarity_for_g
from rankings import generate_p_user, editorial_categories

# First run will assume that all users have the same patience,
# which will be set at start up through a passing argument,
# or randomly chosen for all users.

user_patience = 0.5

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pu = generate_p_user(100)
    np.random.shuffle(pu)

    pprint("User List: \n")
    pprint(pu)

    # recall = calculate_user_recall_for_g_in_k(pu, editorial_categories[0], 20)
    # rbp = calculate_rank_biased_precision(user_patience, 20)
    familiarity = calculate_user_familiarity_for_g(pu, editorial_categories[0], user_patience)
    print(f"familiarity", familiarity)
