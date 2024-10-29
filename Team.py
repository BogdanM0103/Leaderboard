import random

from EntityBase import EntityBase
from tools import generate_id, config, generate_random_team


class Team(EntityBase):
    NAME = ["red", "blue"]

    def __init__(self):
        self.name = random.choice(Team.NAME)
        if self.name not in self.NAME:
            raise ValueError(f"Invalid Team Name ${self.name}. It must be 'red' or 'blue'.\n")
        self.players = generate_random_team()
        self.status = self.set_random_status()
        super().__init__(entity_type = "team")

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

    def get_players(self):
        return self.players

    # Setter for the status of the team
    def set_random_status(self):
        return random.choice(['win', 'loss'])

    # Getter for status of the team
    def get_status(self):
        return self.status
