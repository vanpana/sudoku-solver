class State:
    def __init__(self, values):
        self.__values = values

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    def interchange_positions(self, first_pos, second_pos):
        values = []

        for index in range(0, len(self.__values) + 1):
            if index == first_pos:
                values.append(self.__values[second_pos])
            elif index == second_pos:
                values.append(self.__values[first_pos])
            else:
                values.append(self.__values[index])

        return values
