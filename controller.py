from model import Model
from view import *

class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View(self)

    def onButtonClick(self,caption):
        if caption == "buttonSubmit":
            print("got button Press info from view in Controller")
            self.model.LoginID= self.view.LoginFrame.getEntryValue(0)
            self.model.password=self.view.LoginFrame.getEntryValue(1)
            print("Connecting and validating User in DataBase")




# State
# defines an interface for encapsulating the behavior associated
# with a particular state of the Context
#
class State(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.controller1=Controller()
    def handle(self):
        pass
#
# Concrete States
# each subclass implements a behavior associated with a state
# of the Context
#
class ConcreteStateLogin(State):
    def __init__(self):
        State.__init__(self)

    def handle(self):
        self.controller1.view.loginPage()
        print("Login Displayed")


class ConcreteStateProfile(State):
    def __init__(self):
        State.__init__(self)

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
    MyController = Controller()
    DisplayProfile = ConcreteStateProfile()
    context = Context()
    print("-------------------------------Setting state to display Login Page ---------------------")
    context.setState(DisplayLogin)
    context.request()



    #context.setState(DisplayProfile)
    #context.request()




