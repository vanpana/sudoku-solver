import copy


class State:
    def __init__(self, values):
        self.__values = values
        self.__illegal_values = []
        self.__coordinates = []

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    @property
    def illegal_values(self):
        return self.__illegal_values

    @illegal_values.setter
    def illegal_values(self, value):
        self.__illegal_values = value

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    def interchange_positions(self, first_pos, second_pos):
        values = []

        for index in range(0, len(self.__values)):
            if index == first_pos:
                values.append(self.__values[second_pos])
            elif index == second_pos:
                values.append(self.__values[first_pos])
            else:
                values.append(self.__values[index])

        return State(values)

    def fill_in(self, number, pos):
        possible_state = copy.deepcopy(self)
        possible_state.values[pos] = number

        inserted_line, inserted_col = possible_state.coordinates[pos]

        for counter in range(0, len(possible_state.coordinates)):
            line, col = possible_state.coordinates[counter]
            if line == inserted_line or col == inserted_col:
                possible_state.illegal_values[counter].add(number)
        return possible_state

    def __len__(self):
        return len(self.__values)

    def __getitem__(self, item):
        return self.__values[item]

    def __eq__(self, other):
        return self.__values == other.values

    def __str__(self):
        return str(self.__values)

    def __repr__(self):
        return str(self)