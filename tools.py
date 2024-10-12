import random
import os

ID_FILE = "generated_ids.txt"
NAME_FILE = "usernames_list.txt"

def load_generated_ids():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, "r") as file:
            return {int(line.strip()) for line in file}
    return set()

def save_generated_id(new_id):
    with open(ID_FILE, "a") as file:
        file.write(f"{new_id}\n")

list_id = load_generated_ids()
list_names = load_names()
def generateID():
    while True:
        new_id = random.randint(100000, 999999)
        if new_id not in list_id:
            list_id.add(new_id)
            save_generated_id(new_id)
            return new_id