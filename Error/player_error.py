

class EmptyNameException(Exception):
    """Raise if name is empty"""
    pass

class WrongAgeException(Exception):
    """Raise if age gets caught by ValueError"""
    pass

class InvalidAgeException(Exception):
    """Raise if age is not in the valid range"""
    pass

class EmptyAdressException(Exception):
    """Raise if Adress is empty"""
    pass

class EmptyEmailException(Exception):
    """Raise if Email is Empty"""
    pass

class InvalidEmailException(Exception):
    """Raise if Email necessary"""
    pass

class EmptyLinkException(Exception):
    """Raise if Link is empty"""
    pass

class EmptyHandleException(Exception):
    """Raise if Handle is empty"""
    pass

class InvalidCharacterHandle(Exception):
    """Raise if invalid characters are in handle"""
    pass

class HandleExistsException(Exception):
    """Raise if handle is already in use"""
    pass
