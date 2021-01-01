from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View(self)


    def main(self):
        print("In main of controler")
        self.view.main()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()