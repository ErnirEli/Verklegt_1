from models.tournament import Tournament
from models.match import Match
from models.schedule import Schedule
from Datalayer.data_api import DataAPI

class ScheduleLogic():

    def __init__(self):
        self._data_api = DataAPI()

    def create_tournament_schedule(self, tournament):
        Schedule(tournament)
        return
    
    def update_schedule(self, change: Match) -> None:
        matches = self._data_api.get_all_matches()

        for match in matches:
            match: Match

            a = match.team_a.split()
            b = match.team_b.split()

            if len(b) == 4 or len(a) == 4:
                if a[0] == "Winner":
                    if int(a[3]) == change.match_number:
                        match.team_a = change.winner
                        break

                if b[0] == "Winner":
                    if int(b[3]) == change.match_number:
                        match.team_b = change.winner
                        break

        self._data_api.write_match(matches)
        return
    
    def get_active_round(self, tournament) -> list:
        tournament: Tournament
        matches = self._data_api.get_all_matches()

        for match in matches:
            match: Match

            if match.tournament_id == tournament.id and match.state == False:
                return match



