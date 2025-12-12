
class ClubNameExistsError(Exception):
    '''Raise if created club does not have a unique name'''
    pass


class ColorNotAvailable(Exception):
    '''Raise if created club wants a color that is not valid'''
    pass

class TeamAlreadyInClubError(Exception):
    '''Raise if team is already in club'''
    pass


class TeamDoesNotExistError(Exception):
    '''Raise if wanted team to a club does not exist'''
    pass

class InvalidNumOfTeams(Exception):
    '''Raise if cllub wants more than 5 teams or less than 1 team'''
    pass

class TeamNotAvailableError(Exception):
    '''Raise if a club wants a team that is already in a club'''
    pass

class ClubDoesNotExist(Exception):
    '''Raise if user inputs a club name that does not exist'''
    pass