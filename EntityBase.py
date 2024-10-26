import json
import os
from abc import ABC

from tools import generate_id, config


class EntityBase(ABC):
    def __init__(self, entity_type):
        self.id = generate_id(for_what = entity_type)
        self.entity_type = entity_type
        self.write_file()
    def get_id(self):
        return self.id
    def to_dict(self):
        base_dict = {
            f"{self.entity_type}_id": self.id,
        }
        match self.entity_type:
            case "player":
                base_dict.update({
                    "player_name": getattr(self, "name", "Unknown"),
                })
            case "team":
                base_dict.update({
                    "team_name": getattr(self, "name", "Unknown"),
                    "team_players": [
                        player.to_dict() if hasattr(player, "to_dict") else player
                        for player in getattr(self, "players", [])
                    ],
                    "team_status": getattr(self, "status", ""),
                })
        return base_dict

    def write_file(self):
        folder = config[f"{self.entity_type}s_folder"]
        if not folder:
            os.makedirs(folder)
        file = os.path.join(folder, f"{self.id}.json")
        with open(file, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
        print(f"Wrote {file} for {self.entity_type} with id: {self.id}\n")