import sqlite3
import logging
from PasswordManagerExceptions import *
from UI import UI
from Encryption import Encryption
from MasterKey import check
from clicks_util import logger

'''c.execute("""CREATE TABLE passwords(
            name text,
            password text,
            url text
    )""")'''

class PasswordManager:

    #TODO: create password function
    #TODO: add create_password function to run

    #TODO: delete things from database

    def __init__(self):
        self.lg = logging.getLogger(__name__)

        self.conn = sqlite3.connect("passwords.db")

        self.c = self.conn.cursor()

        from Encryption import Encryption

        self.en = Encryption()
        pass

    def create_table(self):

        self.c.execute("""CREATE TABLE passwords (
        name text,
        password text,
        url text
        )""")

        self.conn.commit()

    def get_name(self, name):

        return name

    def get_password(self, name):

        try:
            #self.c.execute(f"SELECT password FROM passwords WHERE name='{self.en.encrypt(name)}'")
            self.c.execute(f"SELECT password FROM passwords WHERE name='{name}'")

            entries = list(self.c.fetchone())
            return entries[0]

        except Exception as e:

            lg.error(e)

    def get_url(self, name):

        try:
            #self.c.execute(f"SELECT url FROM passwords WHERE name='{self.en.encrypt(name)}'")
            self.c.execute(f"SELECT url FROM passwords WHERE name='{name}'")

            entries = list(self.c.fetchone())
            return entries[2]

        except Exception as e:

            lg.error(e)

    def get_all(self, name):

        try:
            #self.c.execute(f"SELECT * FROM passwords WHERE name='{self.en.encrypt(name).decode()}'")
            self.c.execute(f"SELECT * FROM passwords WHERE name='{name}'")

            entries = list(self.c.fetchone())
            return entries

        except Exception as e:

            lg.error(e)

    def remove_password(self, name):

        try:
            text_to_delete = f"DELETE FROM passwords WHERE name='{name}'"
            self.c.execute(text_to_delete)
            self.conn.commit()

        except Exception as e:

            lg.error(e)

    def write_password(self, name, password, url):

        try:
            if not url:
                #text_to_insert = f"INSERT INTO passwords VALUES ('{self.en.encrypt(name).decode()}', '{self.en.decrypt(password).decode()}', 'None')"
                text_to_insert = f"INSERT INTO passwords VALUES ('{name}', '{password}', 'None')"
                self.lg.info(text_to_insert)
                self.c.execute(text_to_insert)

            else:
                #text_to_insert = f"INSERT INTO passwords VALUES ('{self.en.encrypt(name).decode()}', '{self.en.encrypt(password).decode()}', '{self.en.encrypt(url).decode()}')"
                text_to_insert = f"INSERT INTO passwords VALUES ('{name}', '{password}', '{url}')"
                self.lg.info(text_to_insert)
                self.c.execute(text_to_insert)

            self.conn.commit()

        except Exception as e:

            self.lg.error(e)

    def run(self):

        not_search_terms = ["MasterKey"]

        ui = UI()
        ui.build_start()

        pm = PasswordManager()
        if check(pm.get_password("MasterKey")):

            print(f"""
Your MasterKey was recognised by the database file, please continue
        """)

        else:
            print(f"""
Your MasterKey was not recognised by the database file
        """)

            #raise FalseMasterKey

        while True:

            action = str(input("PasswordManager >>> "))
            action_list = action.split(" ")

            ui.delete_input()

            if len(action_list) < 1:

                raise NotEnoughAttributes

            elif action_list[0] == "r":

                if len(action_list) > 2:

                    raise TooManyAttributes

                elif action_list[1] in not_search_terms:

                    raise ForbiddenSearchTermError

                else:
                    entries = self.get_all(action_list[1])
                    ui.build_response(entries)

            elif action_list[0] == "w":

                if len(action_list) < 3:

                    raise NotEnoughAttributes

                elif action_list[1] in not_search_terms:

                    raise ForbiddenSearchTermError

                elif len(action_list) == 3:
                    self.write_password(action_list[1], action_list[2], "None")

                elif len(action_list) == 4:

                    self.write_password(name=str(action_list[1]), password=str(action_list[2]), url=str(action_list[3]))

                elif len(action_list) > 4:

                    raise TooManyAttributes

            elif action_list[0] == "rm":

                try:
                    if len(action_list) < 2:

                        raise NotEnoughAttributes

                    elif action_list[1] in not_search_terms:

                        raise ForbiddenSearchTermError

                    else:
                        self.remove_password(action_list[1])
                        print(f"Removed {action_list[1]} from table")

                except Exception as e:

                    lg.error(e)
