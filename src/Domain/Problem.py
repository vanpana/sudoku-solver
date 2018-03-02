class Problem:
    def __init__(self, filename):
        self.__matrix_size = 0
        self.__matrix = []
        self.__initialState = []
        self.__missing_numbers = []
        self.__filename = filename

        # Read problem data
        result = self.__read_from_file()

        # Set missing numbers if read was successful
        if result:
            self.__set_missing_numbers()

    def heuristic(self, first_state, second_state):
        pass  # TODO: implement heuristic -> return float

    def expand(self, state):
        states = []

        for first_index in range(0, len(state.values)):
            for second_index in range(first_index, len(state.values) + 1):
                if state.values[first_index] < state.values[second_index]:
                    child = state.interchange_positions(first_index, second_index)
                    if child not in states:
                        states.append(child)

        return states
        pass  # TODO: implement expand -> return list of states

    def __read_from_file(self):
        """
        Reads from file and creates matrix.
        :rtype: boolean
        """
        try:
            with open(self.__filename, "r") as file:
                for line in file:
                    line = line.strip("\n")

                    if len(line) == 1:
                        self.__matrix_size = int(line)
                    else:
                        line = line.split(",")

                        self.__matrix.append([])
                        for number in line:
                            try:
                                self.__matrix[len(self.__matrix) - 1].append(int(number))
                            except TypeError:
                                return False

            if self.__matrix_size == 0:
                return False
            return True
        except FileNotFoundError:
            return False

    def __set_missing_numbers(self):
        """
        Sets missing numbers from the matrix to the missing_numbers list
        """
        frequency = {}
        for i in range(1, self.__matrix_size + 1):
            frequency[i] = self.__matrix_size

        for line in self.__matrix:
            for number in line:
                if number != 0:
                    frequency[number] -= 1

        for number in frequency.keys():
            while frequency[number]:
                self.__missing_numbers.append(number)
                frequency[number] -= 1

    def is_valid(self):
        return self.__matrix_size != 0 and len(self.__missing_numbers) != 0
