class Problem:
    def __init__(self, values, initial_state, final_state):
        self.__values = values
        self.__initialState = initial_state
        self.__finalState = final_state

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values

    @property
    def initial_state(self):
        return self.__initialState

    @initial_state.setter
    def initial_state(self, value):
        self.__initialState = value

    @property
    def final_state(self):
        return self.__finalState

    @final_state.setter
    def final_state(self, value):
        self.__finalState = value

    def heuristic(self, first_state, second_state):
        pass  # TODO: implement heuristic -> return float

    def expand(self, state):
        pass  # TODO: implement heuristic -> return list of states

    def read_from_file(self, filename):
        pass  # TODO: read from file -> return boolean