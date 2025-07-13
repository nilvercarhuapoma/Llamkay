import os
import pickle
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = os.path.join('credenciales', 'credentials.json')


def get_token_path(user_id):
    return os.path.join('credenciales', f'token_{user_id}.pickle')


def build_flow():
    return Flow.from_client_secrets_file(
        CREDENTIALS_FILE,
        scopes=SCOPES,
        redirect_uri='http://localhost:8000/oauth2callback/'
    )


def save_token(creds, user_id):
    token_path = get_token_path(user_id)
    with open(token_path, 'wb') as token:
        pickle.dump(creds, token)


def load_token(user_id):
    token_path = get_token_path(user_id)
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            return pickle.load(token)
    return None
