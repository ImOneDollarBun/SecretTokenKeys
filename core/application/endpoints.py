from fastapi import APIRouter
from core.application.schemas import SchemaSecret
from core.crud import add_secret, get_secrets, delete_secret

rout = APIRouter()


@rout.post('/secret')
def create_secret(data: SchemaSecret):
    res = add_secret(secret=data.secret, ttl_seconds=data.ttl_seconds, pass_phrase=data.passphrase)
    return {'secret_key': res}


@rout.get('/secret/{secret_key}')
def victoria_secrets(secret_key):
    res = get_secrets(token=secret_key)
    return {'secret': res}


@rout.delete('/secret/{secret_key}')
def blow_up_secret(secret_key):
    res = delete_secret(secret_key)
    return {'status': 'secret_deleted'}
