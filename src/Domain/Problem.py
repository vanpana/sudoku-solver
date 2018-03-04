import copy

from Domain.State import State


class Problem:
    def __init__(self, filename):
        self.__matrix_size = 0
        self.__matrix = []
        self.__initial_state = None
        self.__filename = filename

        # Read problem data
        result = self.__read_from_file()

        # Set missing numbers if read was successful
        if result:
            self.__set_missing_numbers()

            if self.__initial_state is not None:
                self.__set_illegal_values()
                self.__set_coordinates_missing_numbers()

    @property
    def initial_state(self):
        return self.__initial_state

    def heuristic(self, first_state, second_state):
        pass  # TODO: implement heuristic -> return float

    def expand(self, state):
        states = []

        for number in state.missing_numbers:
            for counter in range(0, len(state)):
                if state[counter] is None and\
                        number not in state.illegal_values[counter]:
                    possible_state = state.fill_in(number, counter)
                    if possible_state not in states:
                        states.append(possible_state)

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

        missing_numbers = []
        for number in frequency.keys():
            while frequency[number]:
                missing_numbers.append(number)
                frequency[number] -= 1

        self.__initial_state = State([None for _ in range(0, len(missing_numbers))])
        self.__initial_state.missing_numbers = missing_numbers

    def __set_coordinates_missing_numbers(self):
        coordinates = []
        for line in range(0, len(self.__matrix)):
            for column in range(0, len(self.__matrix[line])):
                if self.__matrix[line][column] == 0:
                    coordinates.append((line, column))

        self.__initial_state.coordinates = coordinates

    def is_valid(self):
        return self.__matrix_size != 0 and len(self.__initial_state.missing_numbers) != 0

    def fill_matrix(self, state):
        counter = 0
        filled_matrix = []

        if None in state:
            return []

        for line in self.__matrix:
            new_line = []
            column_counter = 0
            for element in line:
                # If position is empty, change it from the child
                if element == 0:
                    if state[counter] in new_line or\
                            state[counter] in [row[column_counter] for row in filled_matrix]:
                        return []
                    element = state[counter]
                    counter += 1

                # Create the line
                new_line.append(element)
                column_counter += 1
            filled_matrix.append(new_line)

        return filled_matrix

    def __set_illegal_values(self):
        illegal_values = []
        for line in self.__matrix:
            counter = 0
            for col in line:
                if col == 0:
                    illegal_values.append([])
                    illegal_values[len(illegal_values) - 1].extend(set(line))
                    illegal_values[len(illegal_values) - 1].extend([row[counter] for row in self.__matrix])
                    illegal_values[len(illegal_values) - 1] = set(illegal_values[len(illegal_values) - 1])
                counter += 1

        self.__initial_state.illegal_values = illegal_values


    @staticmethod
    def __check_duplicate_elements_line_col(matrix):
        for line in matrix:
            if not len(line) == len(set(line)):
                return False

        for column in [[row[i] for row in matrix] for i in range(len(matrix))]:
            if not len(column) == len(set(column)):
                return False

        return True

    def check_solution(self, state):
        filled_matrix = self.fill_matrix(state.values)

        if len(filled_matrix) == 0:
            return False

        return self.__check_duplicate_elements_line_col(filled_matrix)

        # TODO: Check 3x3 rows

    def __eq__(self, other):
        return self.__initial_state == other.initial_state
