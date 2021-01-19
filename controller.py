from model import Model
from model import Subscriber
from view import View
from model import Publisher



class Controller:
    def __init__(self):
        self.model=Model()
        self.view=View(self)
        print("Controller Class initiated")


    def onButtonClick(self,caption):
        if caption =="buttonSubmit":
            self.model.pub.add_newsletter("Tech")
            self.model.pub.register(newsletter="Tech", who=s1)
            self.model.recogniseButton(caption)
        if caption == "buttonAddCourse":
            print(f' Course Page {caption} registered')
            self.model.recogniseButton(caption)
        if caption == "buttonSelect":
            print(f' Course Page {caption} registered')
            self.model.SubjectsEnrolled.append()







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

class ConcreteStateAddCourse(State):
    def __init__(self):
        State.__init__(self)

    def handle(self):
        self.controller1.view.CoursesPage()
        print("Courses Displayed")

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
    MyController = Controller()
    DisplayProfile = ConcreteStateProfile()
    DisplayLogin = ConcreteStateLogin()
    DisplayAddCourse=ConcreteStateAddCourse()
    context = Context()
    s1 = Subscriber()
    s1.addSubName("Tom")

    state ="Login"

    while(True):

        print(state)
        if state =="Login":
            context.setState(DisplayLogin)
            context.request()
            print("-------------------------------Setting state to display Login Page ---------------------")
            state = s1.get_data()
            #print(f' In while loop{state} registered')

        if state =="Profile":
            context.setState(DisplayProfile)
            context.request()
            print("-------------------------------Setting state to display Profile Page ---------------------")

        if state =="AddCourse":
            context.setState(DisplayAddCourse)
            context.request()
            print("-------------------------------Setting state to display AddCourse Page ---------------------")







