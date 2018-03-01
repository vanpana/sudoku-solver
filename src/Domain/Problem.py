from Domain.State import State


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
        pass  # TODO: implement heuristic -> return list of states

    def __read_from_file(self):
        """
        Reads from file and creates matrix.
        :rtype: boolean
        """
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

        print(self.__missing_numbers)
