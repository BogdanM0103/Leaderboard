from tools import generate_random_team


class Match:
    def __init__(self, team_1, team_2, winner):
        self.id = id
        self.team_1 = team1
        self.team_2 = team_2
        self.winner = None
        self.loser = None

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

    def generate_random_team(self):
        team = []

