class Match:
    def __init__(self, match_teams: tuple) -> None:
        self.match_teams = match_teams
    
    def __str__(self) -> str:
        return f"teams playing: {self.match_teams[0]} vs {self.match_teams[1]}"