# Requirements:
# games get created automatically
# Organizer inputs match results
# System uptades schedule after results

from Datalayer.data_api import DataAPI
from models.match import Match
from logic.schedule_logic import ScheduleLogic
from tournament_logic import TournamentLogic


class MatchLogic:

    def __init__(self) -> None:

        self._data_api = DataAPI()
        self._schedule = ScheduleLogic()
        self._tournament = TournamentLogic()

    def list_all_matches(self) -> list:

        return self._data_api.get_all_matches()

    def update_game_results(self, match_id, tour_id, score_a, score_b) -> None:
        matches: list = self._data_api.get_all_matches()

        for match in matches:
            match: Match
            if match.match_number == match_id and match.tournament_id == tour_id:
                match.a_score = score_a
                match.b_score = score_b
                match.state = True
                
                if score_a > score_b:
                    match.winner = match.team_a

                else:
                    match.winner = match.team_b

                break

        self._data_api.write_match(matches)
        self._schedule.update_schedule(match)


        if match.round == "Final":
            self._tournament.tournament_results(match)


        return
    
    def update_game_teams(self):
        return
    
    def get_game(self):
        return