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
        return f"{self.match_number:^71}\n{self.team_a:^30}{self.a_score:<4} v {self.b_score:>4}{self.team_b:^30}\n\n{self.date:>34} / {self.time:<34}\n\n{"-"*71}"
    