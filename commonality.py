from pprint import pprint


def calculate_recall(pu, g, k):
    g_el_pu = 0
    g_el_k = 0

    for j in range(len(pu)):
        if g in pu[j]["tags"]:
            g_el_pu += 1

    for i in range(k):
        if g in pu[i]["tags"]:
            g_el_k += 1
    return g_el_k / g_el_pu if g_el_pu else 0


def calculate_familiarity_u_g(pu, g):
    familiarity = 0
    for i in range(len(pu)):
        familiarity += calculate_recall(pu, g, i)

    return familiarity
