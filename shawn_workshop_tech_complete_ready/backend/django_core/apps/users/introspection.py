from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import jwt, os
from django.conf import settings

@api_view(['POST'])
@permission_classes([AllowAny])
def token_introspect(request):
    token = request.data.get('token')
    if not token:
        return Response({'active': False}, status=400)
    try:
        payload = jwt.decode(token, os.getenv('API_SECRET_KEY', settings.SECRET_KEY), algorithms=['HS256'])
        return Response({'active': True, 'payload': payload})
    except Exception as e:
        return Response({'active': False, 'error': str(e)})
