import json
import os
import random
from pickle import FALSE, TRUE

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

    """def to_dict(self):
        return {
            "team_id": self.id,
            "team_name": self.name,
            "team_players": self.players,
            "team_status": self.status
        }"""

    """def write_team_file(self):
        folder_path = "data/teams"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, f"{self.get_id()}.json")
        with open(file_path, "w", encoding = "utf-8") as file:  # Changed from folder_path to file_path
            json.dump(self.to_dict(), file, indent = 4)
        print(f"Wrote team file for {self.get_id()} to {file_path}\n")"""


    # Setter for the status of the team
    def set_random_status(self):
        return random.choice(['win', 'loss'])

    # Getter for status of the team
    def get_status(self):
        return self.status
