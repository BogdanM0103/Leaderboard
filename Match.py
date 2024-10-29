from tools import load_random_team, have_common_players


class Match:
    def __init__(self):
        while True:
            self.team_1 = load_random_team()
            self.team_2 = load_random_team()
            if not have_common_players(self.team_1, self.team_2):
                break
        self.set_winner(self.team_1, self.team_2)
        self.set_loser(self.team_1, self.team_2)
        super().__init__(entity_type = "match")

    def set_winner(self, team_1, team_2):
        # Check if both teams have equal status
        if self.team_1.status == self.team_2.status == "win" or self.team_1.status == self.team_2.status == "loss":
            raise ValueError(f"Both teams have status ${self.team_1.status}")
        elif self.team_1.status == "win":
            self.winner = team_1
            self.loser = team_2
        elif self.team_2.status == "win":
            self.winner = team_2
            self.loser = team_1

    def set_loser(self, team_1, team_2):
        if self.team_1.status == self.team_2.status == "win" or self.team_1.status == self.team_2.status == "loss":
            raise ValueError(f"Both teams have status ${self.team_1.status}")
        elif self.team_1.status == "loss":
            self.winner = team_2
            self.loser = team_1
        elif self.team_2.status == "loss":
            self.winner = team_1
            self.loser = team_2