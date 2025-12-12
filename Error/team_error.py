
class TeamExistsError(Exception):
    '''Raise if created team does not have a unique name'''

class CaptainNotExistError(Exception):
    '''Raise if selected captain does not exist'''

class InvalidWebLink(Exception):
    '''Raise if web link does not contain a dot'''

class TooManyPlayersError(Exception):
    '''Raise if team wants to have more than 5 players'''
    pass

class NotEnoughPlayersError(Exception):
    '''Raise if created team does not have enough amount of players'''
    pass
class PlayerDoesNotExistError(Exception):
    '''Raise if selected player to a team does not exist'''
    pass
class PlayerAlreadyInTeamError(Exception):
    '''Raise if selected player to a team is already in the team'''
    pass
class CaptainNotInTeamError(Exception):
    '''Raise if selected captain for a team is not in the team'''
    pass
class playerNotAvailableError(Exception):
    '''Raised if selected player is already in a team'''
    pass
class CantRemoveCaptainError(Exception):
    '''Raise if user is trying to remove captain from a team'''
    pass

class TeamDoesNotExist(Exception):
    '''Raise if user is trying to find a team that does not exist'''
    pass