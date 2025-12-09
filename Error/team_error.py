class Emptyinput(Exception):
    '''Raise if input is empty'''

class TeamExistsError(Exception):
    '''Raise if created team does not have a unique name'''

class CaptainNotExistError(Exception):
    '''Raise if selected captain does not exist'''

class InvalidWebLink(Exception):
    '''Raise if web link does not contain a dot'''
