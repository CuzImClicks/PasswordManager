
class EntryNotFoundError(Exception):

    def __init__(self, name, *args, **kwargs):

        if name:
            print(f"Entry '{name}' was not found")

        else:
            print(f"Entry was not found")


class NotEnoughAttributes(Exception):

    def __init__(self):

        print("Not enough attributes")


class TooManyAttributes(Exception):

    def __init__(self):

        print("Too many attributes given")


class FalseMasterKey(Exception):

    def __init__(self):

        print("FalseMasterKey")
        quit()


class ForbiddenSearchTermError(Exception):

    def __init__(self):

        print("You are not allowed to search for that term")