from django.http import JsonResponse
from .models_mpesa import MPesaTransaction
from .models import Sale
import json

def mpesa_callback(request):
    try:
        data = json.loads(request.body.decode())
    except:
        data = request.POST.dict() or {}
    # create transaction log
    tx = MPesaTransaction.objects.create(raw_payload=data)
    # Attempt to parse common STK result format
    try:
        body = data.get('Body') or data.get('Transaction') or data
        stk_callback = body.get('stkCallback') if isinstance(body, dict) else None
        if stk_callback:
            result_code = stk_callback.get('ResultCode')
            checkout_request_id = stk_callback.get('CheckoutRequestID')
            callback_metadata = stk_callback.get('CallbackMetadata', {})
            amount = None
            phone = None
            receipt = None
            for item in callback_metadata.get('Item', []) if isinstance(callback_metadata.get('Item', []), list) else []:
                name = item.get('Name') or item.get('name')
                if 'Amount' in (name or ''):
                    amount = item.get('Value')
                if 'MpesaReceiptNumber' in (name or '') or 'MpesaReceiptNumber' in (item.get('Name') or ''):
                    receipt = item.get('Value')
                if 'PhoneNumber' in (name or ''):
                    phone = item.get('Value')
            tx.amount = amount or 0
            tx.phone = phone
            tx.mpesa_receipt = receipt
            if int(result_code) == 0:
                tx.status = 'paid'
                tx.save()
                # link to sale by invoice no if provided in original request (AccountReference)
                # This requires you to store CheckoutRequestID mapping when initiating STK Push
            else:
                tx.status = 'failed'
                tx.save()
    except Exception as e:
        tx.raw_payload = data
        tx.save()
    return JsonResponse({'status':'ok'})