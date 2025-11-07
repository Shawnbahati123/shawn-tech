from fastapi import APIRouter, HTTPException, Request
from services.payment_client import mpesa_stk_push
from utils.phone import normalize_ke_phone
import os, json, requests

router = APIRouter()

@router.post('/mpesa')
async def initiate_mpesa(payload: dict):
    # payload: {phone, amount, invoice_no, callback_url (optional)}
    phone = payload.get('phone')
    amount = payload.get('amount')
    invoice = payload.get('invoice_no')
    if not phone or not amount or not invoice:
        raise HTTPException(status_code=400, detail='phone, amount, invoice_no required')
    normalized = normalize_ke_phone(phone)
    callback = payload.get('callback_url') or os.getenv('MPESA_CALLBACK_URL') or f"{os.getenv('FASTAPI_BASE','http://localhost:8000')}/payments/mpesa/callback"
    # Call Flask payments service
    try:
        resp = mpesa_stk_push({
            'phone': normalized,
            'amount': amount,
            'account_ref': invoice,
            'callback': callback
        })
        return resp.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/mpesa/callback')
async def mpesa_callback(request: Request):
    data = await request.json()
    # Validate and forward to Django to update sale/payment status
    # Expected structure depends on MPesa; store raw payload
    try:
        django_base = os.getenv('DJANGO_BASE_URL','http://django:8001')
        r = requests.post(f"{django_base}/pos/mpesa-callback/", json={'data': data}, timeout=10)
    except Exception as e:
        return {'status':'error', 'detail': str(e)}
    return {'status':'ok', 'forwarded': r.status_code}
