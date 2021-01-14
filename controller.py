from model import Model
from view import *


class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View(self)



    def main(self):
        print("In main of controller")
        self.view.loginPage()

    def onButtonClick(self,caption):
        if caption == "Button1":
            print("hello")



#
# State
# defines an interface for encapsulating the behavior associated
# with a particular state of the Context
#
class State:
    def handle(self):
        pass


#
# Concrete States
# each subclass implements a behavior associated with a state
# of the Context
#
class ConcreteStateLogin(State,Controller):
    def __init__(self):
        State.__init__(self)
        Controller.__init__(self)
        self.controller1=Controller()

    def handle(self):
        self.controller1.view.loginPage()
        print("Login Displayed")


class ConcreteStateProfile(State,Controller):
    def __init__(self):
        State.__init__(self)
        Controller.__init__(self)
        self.controller1 = Controller()

    def handle(self):
        self.controller1.view.profilePage()
        print("Profile Page displayed")


#
# Context
# defines the interface of interest to clients
#
class Context:
    def __init__(self):
        self._state = State()

    def setState(self, state):
        self._state = state

    def request(self):
        self._state.handle()



if __name__ == '__main__':
    #myApp = Controller()
    #myApp.main()
    DisplayLogin = ConcreteStateLogin()
    DisplayProfile = ConcreteStateProfile()
    context = Context()

    context.setState(DisplayLogin)
    context.request()




