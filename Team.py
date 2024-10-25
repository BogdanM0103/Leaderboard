import json
import os
import random
from pickle import FALSE, TRUE

from tools import generate_id, config


def generate_random_team():
    available_players = []

    # Load players from directory
    players_folder = config['players_folder']
    for filename in os.listdir(players_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(players_folder, filename)
            with open(file_path, 'r') as file:
                player_data = json.load(file)
                # Instead of creating a new player object, just append the data
                available_players.append(player_data)
    # Check if there are enough players for a team
    if len(available_players) < 5:
        raise ValueError("Too few players to form a team")
    # Select 5 unique players
    selected_players = random.sample(available_players, 5)
    # Store selected players
    #self.players.extend(selected_players)

    # Return the selected players
    return selected_players


class Team:
    NAME = ["red", "blue"]

    def __init__(self):
        self.id = generate_id(forWhat ="team")

        self.name = "red"
        if self.name not in self.NAME:
            raise ValueError(f"Invalid Team Name ${self.name}. It must be 'red' or 'blue'.\n")
        self.players = generate_random_team()
        self.status = self.set_random_status()
        self.write_team_file()

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

    def to_dict(self):
        return {
            "team_id": self.id,
            "team_name": self.name,
            "team_players": self.players,
            "team_status": self.status
        }

    def write_team_file(self):
        folder_path = "data/teams"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, f"{self.get_id()}.json")
        with open(file_path, "w", encoding = "utf-8") as file:  # Changed from folder_path to file_path
            json.dump(self.to_dict(), file, indent = 4)
        print(f"Wrote team file for {self.get_id()} to {file_path}\n")


    # Setter for the status of the team
    def set_random_status(self):
        return random.choice(['win', 'loss'])

    # Getter for status of the team
    def get_status(self):
        return self.status

    def get_id(self):
        return self.id

