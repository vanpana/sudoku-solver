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
                self.__set_possible_values()
                self.__set_coordinates_missing_numbers()

    @property
    def initial_state(self):
        return self.__initial_state

    def heuristic(self, first_state, second_state):
        pass  # TODO: implement heuristic -> return float

    def expand(self, state):
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

        self.__initial_state = State([])
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

    def __set_possible_values(self):
        possible_values = []
        illegal_values = []
        line_position = 0
        for line in self.__matrix:
            column_position = 0
            for value in line:
                if value == 0:
                    illegal_values.append([])
                    possible_values.append([])

                    illegal_values[len(illegal_values) - 1].extend(set(line))
                    illegal_values[len(illegal_values) - 1].extend([row[column_position] for row in self.__matrix])
                    illegal_values[len(illegal_values) - 1].extend(self.__get_values_from_square(line_position, column_position))
                    illegal_values[len(illegal_values) - 1] = set(illegal_values[len(illegal_values) - 1])

                    for number in set(self.__initial_state.missing_numbers):
                        if number not in illegal_values[len(illegal_values) - 1]:
                            possible_values[len(possible_values) - 1].append(number)
                    possible_values[len(possible_values) - 1] = set(possible_values[len(possible_values) - 1])

                    if len(possible_values[len(possible_values) - 1]) == 1:
                        # Pop also from missing numbers
                        value = possible_values.pop().pop()
                        illegal_values.pop()
                        self.__matrix[line_position][column_position] = value

                column_position += 1
            line_position += 1

        self.__initial_state.possible_values = possible_values

    def __get_values_from_square(self, line, col):
        values = []
        line_start = (line // 3) * 3
        column_start = (col // 3) * 3
        for line in range(line_start, line_start + 3):
            values.extend(self.__matrix[line][column_start: column_start + 3])

        return set(values)


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

        if not self.__check_duplicate_elements_line_col(filled_matrix):
            return False

        for line in range(0, len(self.__matrix)):
            for col in range(0, len(self.__matrix)):
                if len(self.__get_values_from_square(line, col)) != len(self.__matrix):
                    return False

        return True

    def __eq__(self, other):
        return self.__initial_state == other.initial_state
