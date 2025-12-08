from Datalayer.data_api import DataAPI
from logic.schedule_logic import ScheduleLogic
from models.tournament import Tournament
from models.team import Team
from models.match import Match
from models.player import Player
from models.club import Club
from datetime import date
from datetime import time


class TournamentLogic:
    
    def __init__(self) -> None:
        self._data_api = DataAPI()
        self._schedule = ScheduleLogic()


    def list_all_tournaments(self)-> list:
        return self._data_api.get_all_tournaments()


    def get_tournament(self, tournament_id: str) -> Tournament:
        tournaments = self._data_api.get_all_tournaments()

        for tournament in tournaments:
            tournament: Tournament

            if tournament.id == tournament_id:
                return tournament


    def add_teams(self, teams: list, tournament: Tournament) -> Team:
        all_teams = self._data_api.get_all_teams()

        for team in teams:
            team: Team

            if team.tour_IDs == 'None':
                team.tour_IDs = tournament.name

            else:
                team.tour_IDs += f" {tournament}"

        self._data_api.write_teams(all_teams)

        return
        
    def tournament_schedule(self, tournament: Tournament) -> list:
        matches: list = self._data_api.get_all_matches()

        tournament_matches = []

        for match in matches:
            match: Match

            if match.tournament_id == tournament.id:
                tournament_matches.append(match)

        return tournament_matches
    
    def active_round_schedule(self, tournament: Tournament) -> list:
        round_match: Match = self._schedule.get_active_round()
        all_matches:list = self._data_api.get_all_matches

        active_round_matches: list = []

        for match in all_matches:
            match: Match

            if match.round == round_match.round:
                active_round_matches.append(match)


        return active_round_matches




    def create_a_tournament(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email:str,
                contact_number:str, servers: int):
        
        new_tournament = Tournament(tournament_id, name, venue, start_date, end_date,
                                    contact, contact_email, contact_number, servers)
        self._data_api.add_tournament(new_tournament)
        self._schedule.create_tournament_schedule(new_tournament)
        return
    

    def tournament_bracket(self):
        return
    

    def tournament_results(self, match: Match):
        players = self._data_api.get_all_players()
        teams = self._data_api.get_all_teams()
        clubs = self._data_api.get_all_clubs()

        for player in players:
            player: Player

            if player.team_name == match.team_a or player.team_name == match.team_b:
                if player.team_name == match.winner:
                    player.wins += 1

                else:
                    player.runner_up += 1

                break

        for team in teams:
            team: Team

            if team.name == match.team_a or team.name == match.team_b:
                if team.name == match.winner:
                    team.wins += 1

                else:
                    team.runner_up += 1

                for club in clubs:
                        club: Club

                        if team.club == club.name:
                            club.wins += 1

                        break

                break

        return