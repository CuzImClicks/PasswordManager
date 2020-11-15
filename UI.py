
class UI:

    def __init__(self):

        self.version = "v1 Pre Release 1"

        pass

    def title(self):
        return f"""
Clicks Password Manager - {self.version}
"""

    def help_commands(self):
        return f"""
Welcome to Clicks Password Manager, 
there are two commands available:
r <name> - Read the name, password and url from a entry
w <name> <password> <url> - Create an entry and add it to the database
"""

    def delete_input(self):

        print("\033[H\033[H ")
        print("\033[H ")

    def build_response(self, entries=[]):
        from Encryption import Encryption

        en = Encryption()

        #print(f"{en.decrypt(entries[0])} | {en.decrypt(entries[1])} | {en.decrypt(entries[2])}")
        print(f"{entries[0]} | {entries[1]} | {entries[2]}")

    def build_start(self):

        print(self.title() + self.help_commands())
