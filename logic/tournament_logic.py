from Datalayer.data_api import DataAPI
from models.tournament import Tournament
from models.team import Team
from models.match import Match
from datetime import date
from datetime import time
import random

class TournamentLogic:
    
    def __init__(self) -> None:
        self._data_api = DataAPI()

    def list_all_tournaments(self)-> list:
        return self._data_api.get_all_tournaments()

    def create_tournaments(self, start_date: str, end_date: str, name: str, 
                        venue: str, contract: str, contact_person_email:str, 
                        contact_person_number:str, team_list: list) -> Tournament:  

        tournament: Tournament = Tournament(start_date, end_date, name, venue, 
                                            contract, contact_person_email, 
                                            contact_person_number, team_list)
        
        self._data_api.add_tournament(tournament)

        return tournament


    def add_team(self, team: Team, tournament: Tournament) -> Team:
        team.tournament = tournament.name

        return team
        
        

    def tournament_schedule(self):
        #torunament name    start date      end date
        tournaments = self.get_all_tournaments()
        return tournaments


    
    def tournament_results(self):
        return
    
    def create_a_tournament(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email:str,
                contact_number:str, servers: int):
        
        new_tournament = Tournament(tournament_id, name, venue, start_date, end_date,
                                    contact, contact_email, contact_number, servers)
        self._data_api.add_tournament(new_tournament)
        return
    
    def tournament_bracket(self):
        return
    

    def create_tournament_schedule(self) -> list:
        teams = self._data_api.get_all_teams()
        tournament_teams = []
        for team in teams:
            team: Team
            if "RGeE2" in team.tour_IDs:
                tournament_teams.append(team.name)

        team_amount = len(tournament_teams)
        random.shuffle(tournament_teams)
        #start_date = tournament.start_date
        #end_date = tournament.end_date
        rounds = 3
        n = 1
        while 2 ** rounds <= team_amount:
            rounds += 1
            if 2 ** rounds > team_amount:
                rounds -= 1
                axcess = team_amount - 2 ** rounds
                for loc in range((team_amount - 1), 
                                (team_amount - (axcess * 2)), 
                                -2):
                    print(loc)
                    team_a = tournament_teams[loc]
                    team_b = tournament_teams[loc - 1]

                    game = Match(n, 2, "Playoffs", team_a, team_b)
                    self._data_api.add_match(game)

                    tournament_teams[loc - 1] = f"Winner of game {n}"
                    tournament_teams.remove(tournament_teams[loc])

                    n += 1
                    
                break
        
        if len(tournament_teams) == 64:
            for loc in range(64, 0, -2):

                team_a = tournament_teams[loc]
                team_b = tournament_teams[loc - 1]

                game = Match(n, 2, "R64",team_a, team_b)
                self._data_api.add_match(game)

                tournament_teams[loc - 1] = f"Winner of game {n}"
                tournament_teams.remove(team_a)
                
                n += 1

        if len(tournament_teams) == 32:
            for loc in range(32 - 1, 0, -2):

                team_a = tournament_teams[loc]
                team_b = tournament_teams[loc - 1]

                game = Match(n, 2, "R32",team_a, team_b)
                self._data_api.add_match(game)

                tournament_teams[loc - 1] = f"Winner of game {n}"
                tournament_teams.remove(team_a)
                
                n += 1


        if len(tournament_teams) == 16:
            for loc in range(16 - 1, 0, -2):

                team_a = tournament_teams[loc]
                team_b = tournament_teams[loc - 1]

                game = Match(n, 2, "R16",team_a, team_b)
                self._data_api.add_match(game)

                tournament_teams[loc - 1] = f"Winner of game {n}"
                tournament_teams.remove(team_a)
                
                n += 1

        if len(tournament_teams) == 8:
            for loc in range(8 - 1, 0, -2):

                team_a = tournament_teams[loc]
                team_b = tournament_teams[loc - 1]

                game = Match(n, 2, "Guarter finals",team_a, team_b)
                self._data_api.add_match(game)

                tournament_teams[loc - 1] = f"Winner of game {n}"
                tournament_teams.remove(team_a)
                
                n += 1

        if len(tournament_teams) == 4:
            for loc in range(4 - 1, 0, -2):

                team_a = tournament_teams[loc]
                team_b = tournament_teams[loc - 1]

                game = Match(n, 2, "Semi Finals",team_a, team_b)
                self._data_api.add_match(game)

                tournament_teams[loc - 1] = f"Winner of game {n}"
                tournament_teams.remove(team_a)
                
                n += 1

        if len(tournament_teams) == 2:
            for loc in range(2 - 1, 0, -2):

                team_a = tournament_teams[loc]
                team_b = tournament_teams[loc - 1]

                game = Match(n, 2, "Final",team_a, team_b)
                self._data_api.add_match(game)

                tournament_teams[loc - 1] = f"Winner of game {n}"
                tournament_teams.remove(team_a)
                
                n += 1