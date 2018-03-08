import copy


class State:
    def __init__(self, values):
        self.values = values
        self.missing_numbers = []
        self.possible_values = []
        self.coordinates = []

    # Overrides
    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        return self.values[item]

    def __eq__(self, other):
        return self.values == other.values

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self)