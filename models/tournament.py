
class Tournament:
    
    tournament_id: str
    name: str
    venaue: str
    start_date: str
    end_date: str
    contact: str
    contact_email: str
    contact_number: str

    def __init__(self, tournament_id: str, name: str, venue: str, start_date: str,
                end_date: str, contact: str, contact_email: str,
                contact_number:str, servers: int, state = False) -> None:

        self.id: str = tournament_id
        self.name: str = name
        self.venue: str = venue
        self.start_date: str = start_date
        self.end_date: str = end_date
        self.contact: str = contact
        self.contact_email: str = contact_email
        self.contact_number: str = contact_number
        self.state: bool = state

        self.servers: list = self.generate_server_names(servers)
        
    
    def tournament_to_csv(self) -> list:
        '''Turns a Tournament into list of values for easy csv handeling'''

        return [self.id, self.name, self.venue, self.start_date, self.end_date, self.contact,
                self.contact_email, self.contact_number, len(self.servers), self.state]
    
    def generate_server_names(self, number_of_servers):
        '''Creates names for Tournament servers'''

        servers = []
        number_of_servers = int(number_of_servers)
        for number in range(number_of_servers):

            servers.append(f"{self.id}_Server_{number + 1}")

        return servers
