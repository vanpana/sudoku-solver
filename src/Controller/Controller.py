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

        while to_visit != [] and found is None:
            node = to_visit.pop()
            visited.append(node)
            print(node)

            if None not in node and self.__instance.check_solution(node):
                found = self.__instance.fill_matrix(node)
            else:
                for child in self.__instance.expand(node):
                    if not (child in to_visit or child in visited):
                        to_visit.append(child)

        return found

    def solve_gbfs(self):
        pass  # TODO: solve with gbfs and return a list of states
