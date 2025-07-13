from decouple import config
import os
import pickle
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

# Variables de entorno
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = config('GOOGLE_REDIRECT_URI')
GOOGLE_PROJECT_ID = config('GOOGLE_PROJECT_ID')

# Alcances que vas a usar con Google
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_token_path(user_id):
    return os.path.join('credenciales', f'token_{user_id}.pickle')


def build_flow():
    # Reemplazamos el uso de credentials.json por un diccionario con las variables de entorno
    client_config = {
        "web": {
            "client_id": GOOGLE_CLIENT_ID,
            "project_id": GOOGLE_PROJECT_ID,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": GOOGLE_CLIENT_SECRET,
            "redirect_uris": [GOOGLE_REDIRECT_URI]
        }
    }

    return Flow.from_client_config(
        client_config,
        scopes=SCOPES,
        redirect_uri=GOOGLE_REDIRECT_URI
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
