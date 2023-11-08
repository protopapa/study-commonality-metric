import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

client_id = "fa944f548f4b4ef9ba5ec46f1563d590"
client_secret = "a1c4d42355c54c52ac286330be838045"

# The Spotify API endpoints used by this authorization code
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

scope = ["playlist-modify-public", "user-top-read", "user-read-email", "user-read-private"]


def create_spotify_session():
    return OAuth2Session(client_id, scope=scope, redirect_uri='https://localhost:8888/callback')


def get_user_authorization(session):
    authorization_url, state = session.authorization_url(authorization_base_url)
    print('Please go here and authorize: ', authorization_url)
    return authorization_url


def get_token(session, rrsp):
    auth = HTTPBasicAuth(client_id, client_secret)
    session.fetch_token(token_url, auth=auth, authorization_response=rrsp)
    return session
