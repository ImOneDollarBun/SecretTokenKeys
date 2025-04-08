from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

import base64
import os


class SecureToken:
    def __init__(self, passphrase):
        self.passphrase = bytes(passphrase, encoding='utf-8')

    def _proceed_passphrase(self, salt: bytes):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.passphrase))
        return key

    def encrypt(self, secret: str):
        bytesecret = bytes(secret, encoding='utf-8')
        salt = os.urandom(8)
        key = self._proceed_passphrase(salt)
        cipher_suite = Fernet(key)
        token = cipher_suite.encrypt(bytesecret)
        return token, salt

    def decrypt(self, encrypted_data: bytes, salt: bytes):
        key = self._proceed_passphrase(salt)
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(encrypted_data)


def encode(secret: bytes):
    encoded_secret = base64.urlsafe_b64encode(secret)
    return encoded_secret


def decode(encoded_secret):
    decoded_secret = base64.urlsafe_b64decode(encoded_secret)
    return decoded_secret
