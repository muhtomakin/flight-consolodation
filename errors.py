class Error(Exception):
    """Base class for other exceptions"""
    pass

class DateIsNotInRange(Error):
    pass 

class DateIsNotValid(Error):
    pass

class CityNotValid(Error):
    pass

class ValueTooSmallError(Error):
    pass

class ValueFalse(Error):
    pass

class TripTypeInvalid(Error):
    pass

class TravelersCountChildrenInvalidPerAdults(Error):
    pass