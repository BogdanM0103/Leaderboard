from tools import generateID, assign_random_name

class Player:
    def __init__(self):
        self.name = assign_random_name()
        self.id = generateID()

    def __str__(self):
        return f"{self.name}: {self.id}"

    def get_id(self):
        return self.id