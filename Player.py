from tools import generateID

class Player:
    def __init__(self, name):
        self.name = name
        self.id = generateID()
        self.kills = 0
        self.assists = 0
        self.deaths = 0

    def set_name(self):


    def __str__(self):
        return f"{self.name}: {self.id}"

    def get_id(self):
        return self.id

    def get_kills(self):
        return self.kills

    def get_assists(self):
        return self.assists

    def get_deaths(self):
        return self.deaths