import copy


class State:
    def __init__(self, values):
        self.__values = values
        self.__missing_numbers = []
        self.__illegal_values = []
        self.__coordinates = []

    def fill_in(self, number, pos):
        possible_state = copy.deepcopy(self)
        possible_state.values[pos] = number

        possible_state.__missing_numbers.remove(number)

        inserted_line, inserted_col = possible_state.coordinates[pos]

        for counter in range(0, len(possible_state.coordinates)):
            line, col = possible_state.coordinates[counter]
            if line == inserted_line or col == inserted_col:
                possible_state.illegal_values[counter].add(number)
        return possible_state

    # Getters and setters
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    @property
    def missing_numbers(self):
        return self.__missing_numbers

    @missing_numbers.setter
    def missing_numbers(self, value):
        self.__missing_numbers = value

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

    # Overrides

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