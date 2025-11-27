from django.http import JsonResponse
from django.conf import settings

def validate_api_key(request):
    key = request.headers.get("X-API-KEY")

    if key != settings.API_KEY:
        return JsonResponse({"error": "Invalid API Key"}, status=401)

    return None


from django.db import connection

def call_proc(proc_name, params=()):
    with connection.cursor() as cursor:
        cursor.callproc(proc_name, params)
        if cursor.description:
            result = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in result]
        return None
