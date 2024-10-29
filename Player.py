from EntityBase import EntityBase
from tools import generate_id, assign_random_name

class Player(EntityBase):
    def __init__(self):
        self.name = assign_random_name()
        super().__init__(entity_type = "player")