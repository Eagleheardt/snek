import snekAdapter as adapter

class Command:
    def __init__(self, name, response, action, description):
        self.name = name
        self.response = response
        self.description = description
        self.action = action


