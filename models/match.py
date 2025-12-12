class Match:
    def __init__(self, match_number: int, tournament_id: int, round: str,
                team_a: str, team_b, date: str = "None", time: str = "None",
                server: str = "Server 1", a_score: int = -1, b_score: int = -1,
                winner: str = "None", state = False) -> None:
        
        self.match_number = match_number
        self.tournament_id = tournament_id
        self.round = round
        self.team_a = team_a
        self.team_b = team_b
        self.date = date
        self.time = time
        self.server = server
        self.a_score = a_score
        self.b_score = b_score
        self.winner = winner
        self.state = state

    def match_to_csv(self):
        '''Turns match into list of values for easy CSV handeling'''
        return [self.match_number, self.tournament_id, self.round,
                self.team_a, self.team_b, self.date, self.time,
                self.server, self.a_score, self.b_score,
                self.winner, self.state]
        

    
    def __str__(self) -> str:
        return f"{self.match_number:^59}\n{self.team_a:<25}{self.a_score:<3} vs {self.b_score:>3}{self.team_b:>25}\n{self.date:^29} {self.time:^29}\n"
    