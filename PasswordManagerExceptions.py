import logging

lg = logging.getLogger(__name__)


class EntryNotFoundError(Exception):

    def __init__(self, name, *args, **kwargs):

        if name:
            lg.error(f"Entry '{name}' was not found")

        else:
            lg.error(f"Entry was not found")


class NotEnoughAttributes(Exception):

    def __init__(self):

        lg.error("Not enough attributes")


class TooManyAttributes(Exception):

    def __init__(self):

        lg.error("Too many attributes given")


class FalseMasterKey(Exception):

    def __init__(self):

        lg.error("FalseMasterKey")
        quit()


class ForbiddenSearchTermError(Exception):

    def __init__(self):

        lg.error("You are not allowed to search for that term")