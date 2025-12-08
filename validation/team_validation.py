from Datalayer.data_api import DataAPI

class ValidateTeam:
    def __init__(self):
        pass
    
    def is_captain_or_organizer(self):
        #Á eftir að implementa
        return

    def name_validation(self, name: str):
        if not name:
            return (False, "Team needs to have a name")
        
        team_list = DataAPI.get_all_teams()

        for team in team_list:
            if name.strip() == team.name:
                return (False, "Team already exists")
        
        return True,

    def captain_validation(self, captain):
        if not captain:
            return (False, "Team needs to have a captain")
        if not isinstance(captain, str):
            return (False, "Can't have more than one captain")
        
        return True,
