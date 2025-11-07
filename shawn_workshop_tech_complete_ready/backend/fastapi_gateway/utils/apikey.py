from fastapi import HTTPException, Header
import os

API_KEYS = os.getenv('API_KEYS', '').split(',') if os.getenv('API_KEYS') else []

def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key or x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail='Invalid API key')
    return True
