import jwt, os, datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

SECRET = os.getenv('DJANGO_SECRET_KEY','change_me')

@csrf_exempt
def token_issue(request):
    # Simple username/password token issue
    if request.method != 'POST':
        return JsonResponse({'error':'POST only'}, status=405)
    import json
    data = json.loads(request.body.decode())
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({'error':'invalid credentials'}, status=401)
    payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.role.name if getattr(user,'role',None) else 'user',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    }
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return JsonResponse({'token': token})
