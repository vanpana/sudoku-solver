import os

from Controller.Controller import Controller
from Domain.Problem import Problem
from View.Console import Console


def get_problem(size):
    path = "Data/{0}x{0}.matrix".format(size)
    return Problem(path)


if __name__ == '__main__':
    problem = get_problem(9)
    controller = Controller(problem)
    view = Console(controller)

    view.run()
