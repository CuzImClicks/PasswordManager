from cryptography.fernet import Fernet
from clicks_util import logger
import logging
import string
import random
import os
import hashlib

lg = logging.getLogger(__name__)


class Encryption:

    def create_key(self):

        with open("key.key", "wb+") as f:

            content = Fernet.generate_key()
            f.write(content)
            f.close()

    def get_key(self):

        with open("key.key", "rb+") as f:

            return f.read()
            f.close()

    def encrypt(self, password=""):

        sha = hashlib.sha3_256()
        sha.update(password.encode())
        return sha.digest()



en = Encryption()
