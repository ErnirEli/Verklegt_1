# Requirements:
# games get created automatically
# Organizer inputs match results
# System uptades schedule after results

from Datalayer.data_api import DataAPI
from models.match import Match
from logic.schedule_logic import ScheduleLogic
from logic.tournament_logic import TournamentLogic


class MatchLogic:

    def __init__(self) -> None:

        self._data_api = DataAPI()
        self._schedule_logic = ScheduleLogic()
        self._tournament_logic = TournamentLogic()

    def list_all_matches(self) -> list[Match]:
        '''Takes in nothing and returns a list of all existing amtches of type Match'''

        return self._data_api.get_all_matches()

    def update_game_results(self, change_match: Match, score_a: int, score_b: int) -> None:
        '''Takes in a match of type "Match" and score for team a & b.
        Updates match winner and status and finishes the tournament if match round in "Final".
        Only runs after all validation checks are valid.'''

        matches: list[Match] = self._data_api.get_all_matches()

        for match in matches:
            # Finds the correct match
            if match.match_number == change_match.match_number and match.tournament_id == change_match.tournament_id:
                match.a_score = score_a
                match.b_score = score_b
                match.state = True
                
                # Determines Who the winner is
                if score_a > score_b:
                    match.winner = match.team_a
                else:
                    match.winner = match.team_b

                break

        self._schedule_logic.update_schedule(match)

        # Fininshes tournament if game was a final
        if match.round == "Final":
            self._tournament_logic.tournament_results(match)

        return