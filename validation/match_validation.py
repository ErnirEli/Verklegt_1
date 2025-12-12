from Error.match_error import InvalidScores, DrawError
from Error.general_error import BackButton


class ValidateMatch:
    def __init__(self):
        pass

    def validate_score(self, team_1_score: str, team_2_score: str) -> bool:
        '''Takes in two scores from a match of type str and checks if score is valid.
        raises an error if score is invalid'''
        
        if team_2_score.lower() == "q":
            raise BackButton
        
        team_1_score = int(team_1_score)
        team_2_score = int(team_2_score)

        if team_1_score < 0 or team_1_score > 99:
            raise InvalidScores
        if team_2_score < 0 or team_2_score > 99:
            return InvalidScores
                
        if team_1_score == team_2_score:
            raise DrawError
        
        return True