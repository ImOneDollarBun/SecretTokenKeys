from core.settings import settings
from core.dbCore.logging import log_action

from core.redis_cache.caching import add_cache_key, get_cache_key, delete_cache_key

from core.secure.secure_coding import SecureToken, encode, decode


@log_action(msg='Token is added to cache')
def add_secret(secret: str, pass_phrase: str | None = None, ttl_seconds: int = settings.Global.default_time):
    def set_cache(secret, token, ttl_seconds):
        secret = bytes(secret, encoding='utf-8')
        encoded_secret = encode(secret)
        add_cache_key(encoded_secret, token, ttl_seconds)

    if not pass_phrase:
        pass_phrase = ''

    secure = SecureToken(pass_phrase)
    token, salt = secure.encrypt(secret)

    set_cache(secret, token, ttl_seconds)

    return token


@log_action(msg='Getting token from cache')
def get_secrets(token):
    secret = get_cache_key(token)
    if secret:
        decoded_secret = decode(secret)
        return decoded_secret
    else:
        return 'Token is already used or Deleted'


@log_action(msg='Deleting token from cache')
def delete_secret(token):
    delete_cache_key(token)
