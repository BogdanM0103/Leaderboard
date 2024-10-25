import json
import os
import random

from tools import generate_id, assign_random_name

class Player:
    def __init__(self):
        self.name = assign_random_name()
        self.id = generate_id(for_what="player")
        self.write_player_file()

    def to_dict(self):
        return {
            "player_id": self.id,
            "player_name": self.name
        }

    # This is for creating a file with user information
    def write_player_file(self):
        folder_path = "data/players"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, f"{self.get_id()}.json")
        with open(file_path, "w", encoding = "utf-8") as file:  # Changed from folder_path to file_path
            json.dump(self.to_dict(), file, indent = 4)
        print(f"Wrote player file for {self.get_id()} to {file_path}\n")

    def __str__(self):
        return f"{self.name}: {self.id}"

    def get_id(self):
        return self.id