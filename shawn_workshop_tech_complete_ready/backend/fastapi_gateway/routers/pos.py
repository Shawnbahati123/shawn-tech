from fastapi import APIRouter, Request, HTTPException
from services.django_client import django_post
from utils.auth import get_current_user, rate_limit

router = APIRouter()

@router.post('/sale')
@rate_limit(120)
async def create_sale(request: Request):
    user = get_current_user(request)
    payload = await request.json()
    # attach cashier id from token if not provided
    if 'cashier' not in payload:
        payload['cashier'] = user.get('user')
    resp = django_post('pos/sales/', payload)
    return resp.json()
