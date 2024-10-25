import json
import os
import random
from lib2to3.fixes.fix_asserts import NAMES

# Load configuration from config.json
with open('data/config.json', "r") as config_file:
    config = json.load(config_file)

# This is where the dataset of names is store
NAMES_DATASET_PATH = config['names_dataset']
ID_PLAYERS_PATH = config['id_players']
ID_TEAMS_PATH = config['id_teams']
NAMES_USED_PATH = config['names_used']

# function to generate unique id's
def generate_id(forWhat):
    # the file where id's are written upon creation
    ID_FILE = ID_PLAYERS_PATH if forWhat == "player" else ID_TEAMS_PATH

    # the set that stores existing id's
    existing_ids = set()
    # Adding the existing id's to the set for further use
    try:
        with open(ID_FILE, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:  # Skip empty lines
                    existing_ids.add(int(stripped_line))
    except FileNotFoundError:
        pass
    # Loop that generates id's
    while True:
        new_id = random.randint(100000, 999999)
        if new_id not in existing_ids:
            with open(ID_FILE, "a") as file:
                file.write(f"{new_id}\n")  # Corrected the newline character
            return new_id

def load_names(file_path):
    names_list = set()

    try:
        with open(file_path, "r") as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    names_list.add(stripped_line)
            return names_list
    except FileNotFoundError:
        pass

def assign_random_name():
    names_dataset = NAMES_DATASET_PATH
    names_used = NAMES_USED_PATH
    try:
        with open(names_dataset, "r") as file:
            available_names = set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"File {names_dataset} not found!")
        return None
    used_names = set()
    try:
        with open(names_used, "r") as file:
            used_names = set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"File {names_used} not found!")
        return None
    unused_names = available_names - used_names
    if not unused_names:
        print(f"No available names left")
        return None
    chosen_name = random.choice(list(unused_names))
    with open(names_used, "a") as file:
        file.write(f"{chosen_name}\n")
    return chosen_name

    