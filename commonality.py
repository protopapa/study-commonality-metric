from pprint import pprint


def calculate_user_recall_for_g_in_k(pu, g, k):
    g_el_pu = 0
    g_el_k = 0

    for j in range(len(pu)):
        if g in pu[j]["tags"]:
            g_el_pu += 1

    for i in range(k):
        if g in pu[i]["tags"]:
            g_el_k += 1
    return g_el_k / g_el_pu if g_el_pu else 0


# TODO decide how you do the gama.
def calculate_probability_to_stop_at_rank_i():
    return 1


def calculate_user_familiarity_for_g(pu, g):
    familiarity = 0
    for i in range(len(pu)):
        familiarity += calculate_user_recall_for_g_in_k(pu, g, i)

    return familiarity
