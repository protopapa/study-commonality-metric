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


def calculate_rank_biased_precision(gama, k):
    rbp = (1 - gama) * pow(gama, k - 1)
    return rbp


def calculate_user_familiarity_for_g(pu, g, gama):
    familiarity = 0
    for i in range(len(pu)):
        tr = calculate_user_recall_for_g_in_k(pu, g, i)
        tp = calculate_rank_biased_precision(gama, i)
        familiarity += tp * tr

    return familiarity
