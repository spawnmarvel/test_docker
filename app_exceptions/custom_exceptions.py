

class CustomExceptions(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {"CustomExceptions: "+ arg}



class CustomShutDownExceptions(Exception):
    def __init__(self, arg):
        self.strerror = arg 
        self.args = {"CustomShutDownExceptions: "+ arg}