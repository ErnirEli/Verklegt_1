# það sem er í csv file um matches:
# tournament_id, round, game_number, team1, team2, date, time, server, team1_score, team2_score, winner, state 




class ValidateMatch:
    def __init__(self):
        pass

    def validate_score(self, team_1_score: str, team_2_score: str):
        if team_1_score < 0 or team_1_score > 999 or not team_1_score.isdigit():
            return (False, "Team 1 score is invalid")
        if team_2_score < 0 or team_2_score > 999 or not team_2_score.isdigit():
             return (False, "Team 2 score is invalid")
                
        return True,


    def validate_draw(self, team_1_score: int, team_2_score: int):
        if team_1_score == team_2_score:
            return (False, "Match cant end in a draw, score after extra time: ")
        
        return True,