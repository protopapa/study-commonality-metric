import secrets
import numpy as np

# TODO Fix the random to make more with mainstream
editorial_categories = ["female", "nb", "na", "ea", "ma", "sa", "wa", "me", "ca", "sea", "non-binary"]
main_categories = "mains"

list_ids = ["m", "e"]


# Function that generates a list of Rankings for the given number of users.
# it generates a random Πu for the given size n of users
def generate_users(m=10):
    users = []
    for i in range(m):
        users.append(generate_p_user())
    return users


# Function that creates rankings of size for a user.
# The tags of the songs that are in the list (or you can say the songs are randomly chosen)
def generate_p_user(n=10):
    p = []
    for index in range(n):
        tags = {generate_tag_with_weights()}
        track = {"artist": "s" + str(index), "track": "t" + str(index)}
        pu = {"_id": track, "tags": tags, "i": index}
        p.append(pu)

    return p


# Function that choses tags with a weight 70% for mains and 30%
# for the editorial selected ones. Among the editorial selected ones,
# chooses in a uniform way.
def generate_tag_with_weights():
    random_samples = np.random.choice(list_ids, 10, p=[0.70, 0.30])
    tag_list_output = []
    for r in random_samples:
        if r == list_ids[1]:
            return secrets.choice(editorial_categories)
        if r == list_ids[0]:
            return main_categories
