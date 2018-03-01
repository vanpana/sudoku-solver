import os

from Controller.Controller import Controller
from Domain.Problem import Problem
from View.Console import Console

if __name__ == '__main__':
    problem = Problem("Data/4x4.matrix")
    controller = Controller(problem)
    view = Console(controller)

    view.run()
