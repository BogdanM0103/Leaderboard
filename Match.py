from EntityBase import EntityBase
from tools import load_random_team, have_common_players


class Match(EntityBase):
    def __init__(self):
        while True:
            self.team_1 = load_random_team()
            self.team_2 = load_random_team()
            if not have_common_players(self.team_1, self.team_2):
                break
        super().__init__(entity_type = "match")