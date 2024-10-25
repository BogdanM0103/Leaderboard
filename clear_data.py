import os

from tools import config

def clear_folder(directory):
    # Clear files in the Folder
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print(f"Cleared all files in the {directory} folder")

def clear_file(file):
    if os.path.exists(file):
        with open(file, 'w') as f:
            f.truncate()
        print(f"Cleared {file} file")

def clear_data():
    players_folder = config['players_folder']
    teams_folder = config['teams_folder']
    names_used_file = config['names_used']
    id_players_file = config['id_players']
    id_teams_file = config['id_teams']

    # Clear files in the Players Folder
    for folder in [players_folder, teams_folder]:
        clear_folder(folder)

    # Clear names_used, id_players, id_teams
    for filename in [names_used_file, id_players_file, id_teams_file]:
        clear_file(filename)
clear_data()