from abc import ABC

from tools import generate_id


class EntityBase(ABC):
    def __init__(self, entity_type):
        self.id = generate_id(for_what = entity_type)
    def get_id(self):
        return self.id


