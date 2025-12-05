# requirements:

# name,
# colors,
# hometown,
# country

class ValidateClass:
    def __init__(self):
        pass

    def name_validation(self, name: str):
        if not name:
            return (False, "Club has to have a name")
        
        club_list = DataAPI.get_all_clubs()

        for club in club_list:
            if name.strip() == club.name:
                return (False, "Club already exitst")
            
        return True,

    def validate_colors(self, colors): #colors string eða list?
        if not colors:
            return (False, "Club has to have colors")
        #Eitthvsð fleira?

        return True,

    def validate_hometown(self, hometown: str):
        if not hometown:
            return (False, "Club needs to have a hometown")
        return True,


    def validate_country(self, country: str):
        if not country:
            return (False, "Club needs to have a country")
        return True,

    