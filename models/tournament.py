from models.team import Team
from typing import List

class Tournament:
    start_date: str
    end_date: str
    name: str
    venue: str
    contract: str 
    contact_person_email:str
    contact_person_number:str
    team_list: list
       
    
    def __init__(self, start_date: str, end_date: str, name: str, venue: str, contract: str, contact_person_email:str, contact_person_number:str, team_list: list) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.venue = venue
        self.contract = contract
        self.contact_person_email = contact_person_email
        self.contact_person_number = contact_person_number
        self.team_list = team_list

        self.teams: List[Team] = []

    def tournament_to_csv(self)->list:
        return [self.start_date, self.end_date, self.venue, self.contract, self.contact_person_email, self.contact_person_number, self.team_list]
        
    def __str__(self) ->str:
        return(
            f"The tournament begins: [{self.start_date}]"
            f"The tournament ends:[{self.end_date}]"
            f"The tournament name is [{self.name}]"
            f"The tournament is at [{self.venue}]"
            f"If you need more information contact email: [{self.contact_person_email}], phone: {self.contact_person_number}"
            f"The teams in the tournament:[{self.team_list}]"
        )