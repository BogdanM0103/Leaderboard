import json
import os
from abc import ABC

from tools import generate_id, config


class EntityBase(ABC):
    def __init__(self, entity_type):
        self.id = generate_id(for_what = entity_type)
        self.entity_type = entity_type
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
        return base_dict
