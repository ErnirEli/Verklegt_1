class Club:
    name: str
    colors: str
    hometown: str
    country: str
    
    def __init__(self, name: str, colors: str, hometown: str, country: str):
        self.name = name
        self.colors = colors
        self.hometown = hometown
        self.country = country


    def club_to_csv(self) -> list:
        return [self.name, self.colors, self.hometown, self.country]
    
    def __str__(self) -> str:
        return (
            f"Club name: [{self.name} \n"
            f"club colors: [{self.colors}] \n"
            f"Club hometown: [{self.hometown}] \n"
            f"Club country: [{self.country}]"
        )