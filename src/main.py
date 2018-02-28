from Controller.Controller import Controller
from View.Console import Console

if __name__ == '__main__':
    controller = Controller("")
    view = Console(controller)

    view.run()
