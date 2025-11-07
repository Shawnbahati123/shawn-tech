from fastapi import APIRouter, HTTPException
from utils.jwt_handler import create_token, verify_token

router = APIRouter()

@router.post('/login')
def login(payload: dict):
    # payload: {username, password}
    # TODO: authenticate against Django user API
    if payload.get('username') == 'admin' and payload.get('password') == 'password':
        token = create_token({'user':'admin','role':'admin'})
        return {'token': token}
    raise HTTPException(status_code=401, detail='Invalid credentials')
