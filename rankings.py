import secrets

# TODO Fix the random to make more with mainstream
editorial_categories = ["female", "nb", "na", "ea", "ma", "sa", "wa", "me", "ca", "sea", "non-binary", "mains"]


# Function that creates list/rankings for the given number of users.
# The purpose of this function is purely for testing the rest of the algorithm.
def build_user_p():
    p = []
    for index in range(10):
        tags = {secrets.choice(editorial_categories)}
        track = {"artist": "s" + str(index), "track": "t" + str(index)}
        pu = {"_id": track, "tags": tags, "i": index}
        p.append(pu)

    return p
