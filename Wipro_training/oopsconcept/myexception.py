class AgeException(Exception):
    def __init__(self, errmess):
        super().__init__(errmess)