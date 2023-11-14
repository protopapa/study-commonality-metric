import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

# The Spotify API endpoints used by this authorization code
authorization_base_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"

scope = ["playlist-modify-public", "playlist-modify-public", "user-top-read", "user-read-email", "user-read-private"]


def create_spotify_session(client_id):
    return OAuth2Session(client_id, scope=scope, redirect_uri='https://localhost:8888/callback')


def get_user_authorization(session):
    authorization_url, state = session.authorization_url(authorization_base_url)
    print('Please go here and authorize: ', authorization_url)


def get_token(session, rrsp, client_id, client_secret):
    auth = HTTPBasicAuth(client_id, client_secret)
    return session.fetch_token(token_url, auth=auth, authorization_response=rrsp)
