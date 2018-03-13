import copy


class State:
    def __init__(self, values):
        self.values = values
        self.missing_numbers = []
        self.possible_values = []
        self.coordinates = []

    def fill_in(self, number, pos):
        possible_state = copy.deepcopy(self)
        possible_state.values[pos] = number

        possible_state.possible_values[pos].remove(number)

        inserted_line, inserted_col = possible_state.coordinates[pos]

        for counter in range(0, len(possible_state.coordinates)):
            line, col = possible_state.coordinates[counter]
            if line == inserted_line or col == inserted_col:
                if number in possible_state.possible_values[counter]:
                    possible_state.possible_values[counter].remove(number)
        return possible_state

    # Overrides
    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self.values[item]

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) == tuple:
            return self.values == other[1].values
        return self.values == other.values

    def __lt__(self, other):
        return self.values.count(None) < other.values.count(None)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self)