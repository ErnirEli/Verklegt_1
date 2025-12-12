from models.tournament import Tournament
from models.match import Match
from models.schedule import Schedule
from Datalayer.data_api import DataAPI


class ScheduleLogic():

    def __init__(self):
        self._data_api = DataAPI()


    def create_tournament_schedule(self, tournament):
        '''Creaates a Schedule insteance for tournament'''

        Schedule(tournament)
        return


    def update_schedule(self, change: Match) -> None:
        '''Updates schedule after score update'''

        matches = self._data_api.get_all_matches()

        for match in matches:
            match: Match

            a = match.team_a.split()
            b = match.team_b.split()

            if len(b) == 4 or len(a) == 4 and not match.state:
                if a[0] == "Winner":
                    if int(a[3]) == change.match_number:
                        match.team_a = change.winner
                        break

                elif b[0] == "Winner":
                    if int(b[3]) == change.match_number:
                        match.team_b = change.winner
                        break

        self._data_api.write_match(matches)
        return


    def get_active_matches(self, tournament) -> list[Match]:
        '''Returns a list of all matches from active round'''

        tournament: Tournament
        matches = self._data_api.get_all_matches()
        active = []

        for match in matches:
            match: Match

            if match.tournament_id == tournament.id and match.state == False:
                active_round = match.round
                break

        else:
            return active

        for match in matches:
            match: Match

            if match.round == active_round and match.tournament_id == tournament.id:
                active.append(match)

        return active

    



