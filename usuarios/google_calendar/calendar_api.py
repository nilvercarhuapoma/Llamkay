from googleapiclient.discovery import build
from .auth import load_token

from django.http import JsonResponse

def create_event(summary, start, end):
    creds = load_token()
    if not creds:
        raise Exception("Usuario no autenticado")

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': summary,
        'start': {'dateTime': start, 'timeZone': 'America/Lima'},
        'end': {'dateTime': end, 'timeZone': 'America/Lima'},
    }

    result = service.events().insert(calendarId='primary', body=event).execute()
    return result

