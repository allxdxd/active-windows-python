class WrongOs(Exception):
    def __init__(self, message):
        self.message = message

class NotAdmin(Exception):
    def __init__(self, message):
        self.message = message