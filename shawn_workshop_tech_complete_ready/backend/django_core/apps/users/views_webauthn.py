# WebAuthn placeholder endpoints for registration and authentication
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def start_registration(request):
    # Return a challenge for the client to register a device
    return JsonResponse({'challenge':'dummy-challenge', 'rp':'Shawn Workshop Tech'})

@csrf_exempt
def finish_registration(request):
    # Accept client response, save credential
    return JsonResponse({'status':'ok'})

@csrf_exempt
def start_authentication(request):
    return JsonResponse({'challenge':'dummy-auth-challenge'})

@csrf_exempt
def finish_authentication(request):
    return JsonResponse({'status':'ok', 'user':'demo'})
