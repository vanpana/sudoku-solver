from datetime import time, datetime


class Console:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def __print_menu():
        print("=== Sudoku solver ===\n"
              "1. Solve using BFS\n"
              "2. Solve using GDFS\n"
              "0. Exit\n")

    def run(self):
        if self.__controller.is_valid():
            methods = {1: self.__controller.solve_bfs, 2: self.__controller.solve_gbfs}

            self.__print_menu()

            command = -1

            try:
                command = int(input("Input your command: ").strip("\n"))
            except TypeError:
                print("Must input a valid integer")

            if command == 0:
                exit(0)
            elif command == -1:
                pass
            else:
                start = datetime.now()
                print("Solution is:\n{0}".format(methods[command]()))
                end = datetime.now()
                print("Time elapsed: " + str(end-start))

            self.run()
        else:
            print("Problem is not valid")
