class Team:
    name: str
    captain: str
    web_link: str
    ASCII = str

    def __init__(self,name: str, captain: str, web_link: str, ASCII = str) -> None:
        self.name = name
        self.captain =  captain
        self.web_link = web_link
        self.ASCII = ASCII
    
    def to_list(self) -> list[str, str]:
        return [self.name, self.captain, self.web_link, self.ASCII]
    

    def __str__(self) -> str:
        # User-facing print
        return (
            f"Team name: [{self.name}] "
            f"Team captain: [{self.captain}] "
            f"Team's link to web page [{self.web_link}] "
            f"Team's ASCII logo: [{self.ASCII}] "
        )


    def __repr__(self) -> str:
        # Dev/debug print
        return (
            f"Team(name={self.name}"
            f"captain = {self.captain}"
            f"link to web page = {self.web_link}"
            f"ASCII logo = {self.ASCII}" 
        )