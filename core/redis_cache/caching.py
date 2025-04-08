from core.redis_cache.run_redis import r


def add_cache_key(coded_passphrase: str, token: bytes, ttl_seconds: int):

    """

    :param coded_passphrase: encoded 'secret' data
    :param token: secret_key
    :param ttl_seconds:
    :return:
    """

    if ttl_seconds < 3000:
        ttl_seconds = 3000

    r.set(token, coded_passphrase, ex=ttl_seconds)


def get_cache_key(token):

    """

    :param token: secret_key
    :return:
    """

    secret = r.get(token)
    if secret:
        r.delete(token)

    return secret


def delete_cache_key(token):
    r.delete(token)
