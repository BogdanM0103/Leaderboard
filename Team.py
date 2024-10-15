import os
from pickle import FALSE, TRUE


class Team:
    NAME = ["red", "blue"]

    def __init__(self, name):
        if name not in self.NAME:
            raise ValueError(f"Invalid Team Name ${name}. It must be 'red' or 'blue'.\n")
        self.name = name
        self.players = []
        self.status = ""

    # Adds player
    def add_player(self, player):
        # Checks if there is already enough players
        if len(self.players) >= 5 :
            print(f"Team is already full.\n")
        else:
            # Checks if the player hasn't already been added to the team
            if player not in self.players:
                self.players.append(player)
            self.players.append(player.id)

    # Setter for the status of the team
    def set_status(self, is_winner):
        if is_winner == "win":
            self.status = "win"
        else:
            self.status = "loss"

    # Getter for status of the team
    def get_status(self):
        return self.status

