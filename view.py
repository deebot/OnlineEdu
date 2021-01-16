

class Component():

    def __init__(self, *args, **kw):
        pass
    def getChild(self, index):
        pass

    def add(self, component):
        pass

    def remove(self, index):
        pass

    def operation(self):
        pass


#
# Composite
# defines behavior of the components having children
# and store child components
#
class Composite(Component):
    def __init__(self):
        Component.__init__(self)
        self._children = []

    def getChild(self, index):
        return self._children[index]

    def add(self, component):
        self._children.append(component)
        print("Added new element")

    def remove(self, index):
        self._children.remove(index)

    def operation(self,i):
        #for i in range(len(self._children)):
        #print(self._children[i])
        return self._children[i].operation()


    def setEntryValue(self,i,x):
         self._children[i].setEntryValue(x)

    def getEntryValue(self,i):
        return self._children[i].getEntryValue()


#
# Leaf
# defines the behavior for the elements in the composition,
# it has no children
#
class LeafButton(Component):
    def __init__(self, alias):
        Component.__init__(self)
        self._alias = alias

    def operation(self):
        #print("Leaf----button" + str(self._alias))
        return "button" + str(self._alias)

    def getEntryValue(self):
        pass

class LeafEntry(Component):
    def __init__(self, alias):
        Component.__init__(self)
        self._alias = alias
        self._Evalue="apple"

    def operation(self):
        #print("entry" + str(self._alias))
        return "entry" + str(self._alias)

    def setEntryValue(self,val):
        self._Evalue=val
        print("Value set to " + str(self._Evalue))

    def getEntryValue(self):

        #print("Value is " + str(self._Evalue))
        return self._Evalue

class View(Composite):

    def __init__(self,controller):
        self.controller=controller
        Composite.__init__(self)
        self.LoginFrame=Composite()

    def attachButtonClick(self,x):
        self.controller.onButtonClick(x.operation())

    def loginPage(self):
        print("-----------------------Composing Login Screen ---------------------------------")
        self.LoginFrame.add(LeafEntry("UserID"))
        self.LoginFrame.add(LeafEntry("Password"))
        self.LoginFrame.add(LeafButton("Submit"))
        print("----------------------- Login Screen Composition Done---------------------------")
        print("------------------------Supply Inputs to Login---------------------------------")
        self.LoginFrame.setEntryValue(0,(str(input('Enter the UserID '))))
        self.LoginFrame.setEntryValue(1, (str(input('Enter the Password'))))
        simulate_ButtonPress= str(input("Press Submit Button (y/n)"))
        if simulate_ButtonPress =="y":
            self.controller.onButtonClick(self.LoginFrame.operation(2))

    def profilePage(self):
       # ProfileFrame =Composite()
        print("------------------------Composing Profile Screen-----------------------------")

    def VideoConferencePage(self):
        pass

if __name__ == "__main__":
    pass
   #main =App()
  #  main.loginPage()


