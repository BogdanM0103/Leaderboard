import os
from tools import generateID, assign_random_name

class Player:
    def __init__(self):
        self.name = assign_random_name()
        self.id = generateID()
        self.write_player_file()

    # This is for creating a file with user information
    def write_player_file(self):
        folder_path = "data/players"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, f"{self.get_id()}.txt")
        with open(file_path, "w") as file:  # Changed from folder_path to file_path
            file.write(self.__str__())
        print(f"Wrote player file for {self.get_id()} to {file_path}\n")

    def __str__(self):
        return f"{self.name}: {self.id}"

    def get_id(self):
        return self.id