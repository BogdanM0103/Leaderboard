from pickle import FALSE, TRUE


class Team:
    NAME = ["red", "blue"]

    def __init__(self, name):
        if name not in self.NAME:
            raise ValueError(f"Invalid Team Name ${name}. It must be 'red' or 'blue'.\n")
        self.name = name
        self.players_id = []
        self.status = ""

    def add_player(self, player):
        if(len(self.players_id) >= 5):
            print(f"Team is already full.\n")
        else:
            self.players_id.append(player.id)

    def set_status(self, is_winner):
        if is_winner == "win":
            self.status = "win"
        else:
            self.status = "loss"

    def get_status(self):
        return self.status

