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
    _data_api: DataAPI


    def __init__(self, data_api: DataAPI) -> None:
        self._data_api = data_api
    
    def list_all_teams(self) -> List[Team]:
        """Returns a list of all teams"""
        return self._data_api.get_all_teams()


    def create_team(self, name: str, captain: str, web_link: str = None, ASCII: str = None) -> Team:
        '''creaetes a team only if all validation condition have been met'''
        team: Team = Team(name, captain, web_link, ASCII)
        self._data_api.add_team(team)
        return team
        

    
    def add_player(self, team: Team, new_player: Player):
        team.players.append(new_player)
        self._data_api.add_team(team)
        return team
    
    def remove_player(self, team: Team, unwanted_player: Player):
        team.players.remove(unwanted_player)
        self._data_api.add_team(team)
        return team
    
   
    def team_info(self, team: Team):
<<<<<<< Updated upstream
        return {
            "name": team.name,
            "Captain": team.captain,
            "Players": team.players,
            "Web link": team.web_link,
            "ASCIIlogo": team.ASCII
        }
=======
        players = DataAPI().get_all_players()
        team_players = []
        for player in players:
            if player.team_name == team.name:
                team_players.append(player.handle)
        
        return (
            f"name: {team.name} \n"
            f"Captain: {team.captain} \n"
            f"Players: {team_players} \n"
            f"Web link: {team.web_link} \n"
            f"ASCIIlogo: {team.ASCII} \n"
            f"Tournaments played in: {team.tournament} \n"
            f"Tournaments won: {team.wins}"
        )
>>>>>>> Stashed changes
        
    