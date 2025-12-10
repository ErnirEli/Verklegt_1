from typing import List
from Datalayer.data_api import DataAPI 
from models.team import Team
from models.player import Player


# Requirements:
# Sama lið bara búið til 1 sinni.
# Organizer can register new teams
# team data: name, captain, link to web page, ASCII logo.
# captains add and or change players info



class TeamLogic:

    def __init__(self) -> None:
        self._data_api = DataAPI()
    
    def list_all_teams(self) -> List[Team]:
        '''Returns a list of all teams'''

        return self._data_api.get_all_teams()
    
    def get_team(self, team_name: str) -> Team:
        '''Returns a single team based on team name'''

        teams = self._data_api.get_all_teams()

        for team in teams:
            team: Team

            if team.name == team_name:
                return team

    def create_team(self, name: str, captain: str, web_link: str = None, ASCII: str = None, team_players: list = []) -> Team:
        '''Creates a team only if all validation condition have been met'''

        # Create an instance of team
        team: Team = Team(name, captain, web_link, ASCII)

        # Adds team name to player
        self.add_players(team, team_players)


        self._data_api.add_team(team)

        return team
        

    
    def add_players(self, team: Team, new_players: list):
        '''Adds a selected player to selected team'''

        players = self._data_api.get_all_players()

        # Finds player with the right handle and adds team name to the player
        for player in players:
            if player.handle in new_players:
                player: Player

                player.team_name = team.name

        
        self._data_api.write_players(players)

        return 
    
    def add_player(self, team: Team, wanted_player: Player) -> None:
        '''Adds a Wanted player to a team'''
        
        wanted_player.team_name = team.name

        return
    
    

    def remove_player(self, unwanted_player: Player) -> None:
        '''Removes a selected player out of selected team'''

        unwanted_player.team_name = "None"

        return 
    

    def get_all_players_on_team(self, team: Team) -> list[Player]:
        '''Returns a list of players handles in a team'''

        players = DataAPI().get_all_players()
        team_players = []

        # Adds player handle to list
        for player in players:
            player: Player

            if player.team_name == team.name:
                team_players.append(player.handle)

        return team_players

    def team_info(self, team: Team) -> str:
        '''Gives all info on team'''

        team_players = self.get_all_players_on_team(team)
        
        return (
                f"name: {team.name} \n"
                f"Captain: {team.captain} \n"
                f"Club: {team.club}"
                f"Players: {team_players} \n"
                f"Web link: {team.web_link} \n"
                f"ASCIIlogo: {team.ASCII} \n"
                f"Tournaments played in: {team.tournament} \n"
                f"Tournaments won: {team.wins}")