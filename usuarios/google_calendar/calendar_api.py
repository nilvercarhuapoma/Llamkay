from decouple import config
from googleapiclient.discovery import build
from .auth import load_token
from django.http import JsonResponse

# Variables de entorno por si las necesitas en algún punto
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = config('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = config('GOOGLE_REDIRECT_URI')
GOOGLE_PROJECT_ID = config('GOOGLE_PROJECT_ID')

def create_event(user_id, summary, start, end):
    creds = load_token(user_id)
    if not creds:
        raise Exception("Usuario no autenticado o token no encontrado")

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': summary,
        'start': {'dateTime': start, 'timeZone': 'America/Lima'},
        'end': {'dateTime': end, 'timeZone': 'America/Lima'},
    }

    result = service.events().insert(calendarId='primary', body=event).execute()
    return result
