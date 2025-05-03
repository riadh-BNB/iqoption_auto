class IQOptionConnectionError(Exception):
    """Raised when the client fails to connect to IQ Option."""
    pass

class IQOptionLoginError(Exception):
    """Raised when login credentials are invalid or login fails."""
    pass

class IQOptionTradeError(Exception):
    """Raised when an error occurs during trade execution."""
    pass

class IQOptionBalanceError(Exception):
    """Raised when there is an issue retrieving or parsing balance."""
    pass
