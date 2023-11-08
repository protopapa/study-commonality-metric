def get_user_info(session):
    me = session.get('https://api.spotify.com/v1/me')
    print(me.content)
