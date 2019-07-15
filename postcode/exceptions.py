class InvalidPostCode(Exception):
    """Raise when a postcode is invalid"""
    def __init__(self):
        Exception.__init__(self,"Invalid UK PostCode")