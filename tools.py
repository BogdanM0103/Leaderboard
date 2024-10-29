import json
import os
import random

# Load configuration from config.json
with open('data/config.json', "r") as config_file:
    config = json.load(config_file)

# This is where the dataset of names is store
NAMES_DATASET = config["name_dataset"]
ID_PLAYERS = config["id_players"]
ID_TEAMS = config["id_teams"]
ID_MATCHES = config["id_matches"]
NAMES_USED = config["names_used"]

# function to generate unique id's
def generate_id(for_what):
    # the file where id's are written upon creation
    match for_what:
        case "player":
            ID_FILE = ID_PLAYERS
        case "team":
            ID_FILE = ID_TEAMS
        case "match":
            ID_FILE = ID_MATCHES

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
    names_dataset = NAMES_DATASET
    names_used = NAMES_USED
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

def generate_random_team():
    available_players = []

    # Load players from directory
    players_folder = config['player_folder']
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

def load_random_team():
    teams_folder = config["team_folder"]
    if not teams_folder:
        raise FileNotFoundError("No teams folder found!")
    team_files = [f for f in os.listdir(teams_folder) if f.endswith(".json")]
    if not team_files:
        raise FileNotFoundError("No teams files found!")
    random_team_file = random.choice(team_files)
    random_team_path = os.path.join(teams_folder, random_team_file)
    with open(random_team_path, "r") as file:
        team_data = json.load(file)
    return team_data

def have_common_players(team_1, team_2):
    team_1_ids = {player["player_id"] for player in team_1["team_players"]}
    team_2_ids = {player["player_id"] for player in team_2["team_players"]}
    return team_1_ids.issubset(team_2_ids) or team_2_ids.issubset(team_1_ids)