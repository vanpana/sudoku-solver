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

            try:
                command = int(input("Input your command: "))

                if command == 0:
                    exit(0)
                else:
                    methods[command]()
            except TypeError:
                print("Must input a valid integer")
            self.run()
        else:
            print("Problem is not valid")
