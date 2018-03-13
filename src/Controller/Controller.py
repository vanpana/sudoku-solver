import queue

from Domain.State import State


class Controller:
    def __init__(self, problem):
        self.__instance = problem

    def is_valid(self):
        return self.__instance.is_valid()

    def order_states(self, states):
        pass  # TODO: pass a list of states and return an ordered list of states

    def solve_bfs(self):
        found = None
        visited = []
        to_visit = [self.__instance.initial_state]
        counter = 0

        while to_visit != [] and found is None:
            print(counter, len(to_visit))
            node = to_visit.pop()
            visited.append(node)

            if None not in node and self.__instance.check_solution(node):
                found = self.__instance.fill_matrix(node)
            else:
                for child in self.__instance.expand(node):
                    if not (child in to_visit or child in visited):
                        to_visit.append(child)

            counter += 1

        return found

    def solve_gbfs(self):
        found = None
        visited = []
        to_visit = queue.PriorityQueue()
        to_visit.put((1, self.__instance.initial_state))
        iterable_visit = [(1, self.__instance.initial_state)]

        counter = 0
        while to_visit and found is None:
            print(counter)
            if not to_visit:
                return False

            node = to_visit.get()
            visited.append(node)
            node = node[1]

            if None not in node and self.__instance.check_solution(node):
                found = self.__instance.fill_matrix(node)
            else:
                for child in self.__instance.expand(node):
                    if not (child in iterable_visit or child in visited):
                        heuristic_value = self.__instance.heuristic(child)
                        to_visit.put((heuristic_value, child))
                        iterable_visit.append((heuristic_value, child))
            counter += 1

        return found

        pass  # TODO: solve with gbfs and return a list of states
