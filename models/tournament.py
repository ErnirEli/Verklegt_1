from models.team import Team
from typing import List

class Tournament:
    
    def __init__(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email:str,
                contact_number:str, servers: int) -> None:

        self.id:str = tournament_id
        self.name:str = name
        self.venue:str = venue
        self.start_date:str = start_date
        self.end_date:str = end_date
        self.contact:str = contact
        self.contact_email:str = contact_email
        self.contact_number:int = contact_number

        self.servers:list = self.generate_server_names(servers)
        
    
    def tournament_to_csv(self)->list:
        return [self.id, self.name, self.venue, self.start_date, self.end_date,
                self.contact, self.contact_email, self.contact_number, len(self.servers)]
    
    def generate_server_names(self, number_of_servers):
        servers = []
        
        for number in range(number_of_servers):
            servers.append(f"{self.id}_{number}")

        return servers
    
    def get_tournament_matches():
        pass

        
    def __str__(self) ->str:
        return(
            f"The tournament begins: [{self.start_date}]"
            f"The tournament ends:[{self.end_date}]"
            f"The tournament name is [{self.name}]"
            f"The tournament is at [{self.venue}]"
            f"If you need more information contact email: [{self.contact_person_email}], phone: {self.contact_person_number}"
            f"The teams in the tournament:[{self.team_list}]"
        )