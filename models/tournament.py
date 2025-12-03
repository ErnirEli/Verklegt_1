class Tournament:
    start_date: int
    end_date: int
    name: str
    venue: str
    contract: str 
    contact_person: tuple 
    team_list: list
       
    
    def __init__(self, start_date: int, end_date: str, name: str, venue: str, contract: str, contact_person: tuple, team_list: list) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.venue = venue
        self.contract = contract
        self.contact_person = contact_person
        self.team_list = team_list
        
    def __str__(self) ->str:
        return(
            f"The tournament begins: [{self.start_date}]"
            f"The tournament ends:[{self.end_date}]"
            f"The tournament name is [{self.name}]"
            f"The tournament is at [{self.venue}]"
            f"If you need more information contact: [{self.contact_person}]"
            f"The teams in the tournament:[{self.team_list}]"
        )