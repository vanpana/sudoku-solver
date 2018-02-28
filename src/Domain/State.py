class State:
    def __init__(self, values):
        self.__values = values

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values
