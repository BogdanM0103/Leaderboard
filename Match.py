from EntityBase import EntityBase
from tools import load_random_team, have_common_players


class Match(EntityBase):
    def __init__(self):
        while True:
            self.team_1 = load_random_team()
            self.team_2 = load_random_team()
            if not have_common_players(self.team_1, self.team_2):
                break
        self.set_winner()
        self.set_loser()
        super().__init__(entity_type = "match")
    def set_winner(self):
        if self.team_1 == self.team_2:
            raise ValueError("both teams cannot win or lose!\n")
        elif self.team_1["team_status"] == "win":
            self.winner = self.team_1["team_name"]
        elif self.team_2["team_status"] == "win":
            self.winner = self.team_2["team_name"]
    def set_loser(self):
        if self.team_1 == self.team_2:
            raise ValueError("both teams cannot win or lose!\n")
        elif self.team_1["team_status"] == "loss":
            self.loser = self.team_1["team_name"]
        elif self.team_2["team_status"] == "loss":
            self.loser = self.team_2["team_name"]