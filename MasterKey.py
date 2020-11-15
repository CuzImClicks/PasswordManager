import string
import random
from Encryption import Encryption

en = Encryption()


class MasterKey:

    def create(self):

        content = "".join(random.choices(string.ascii_letters + string.digits, k=64))

        with open("MasterKey.key", "w+") as f:

            f.write(content)
            f.close()

    def get_masterkey(self):

        with open("MasterKey.key", "r") as f:

            return f.read()


def check(masterkey):

    with open("MasterKey.key", "r") as f:

        if masterkey == f.read():

            return True

        else:
            return False
