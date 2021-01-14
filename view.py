

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
        self.entryValue=None

    def getChild(self, index):
        return self._children[index]

    def add(self, component):
        self._children.append(component)
        print("Added a new component"+ str(component))

    def remove(self, index):
        self._children.remove(index)

    def operation(self,index):
        self._children[index].operation()


#
# Leaf
# defines the behavior for the elements in the composition,
# it has no children
#
class ButtonLeaf(Component):
    def __init__(self, index):
        Component.__init__(self)
        self._idx = index

    def operation(self):
        return "Button" + str(self._idx)

class EntryLeaf(Component):
    def __init__(self, index):
        Component.__init__(self)
        self._idx = index
        self._entrydata="d"

    def operation(self):
        print("EntryLeaf " + str(self._idx) + " operation.")

    def setEntryValue(self, edata):
        self._entrydata = edata

    def getEntryValue(self):
        return self._entrydata



class LabelLeaf(Component):
    def __init__(self, index):
        Component.__init__(self)
        self._idx = index

    def operation(self):
        print("LabelLeaf " + str(self._idx) + " operation.")
        return "Button"+str(self._idx)



class View():

    def __init__(self,controller):
        self.controller=controller

    def loginPage(self):
        LoginFrame = Composite()
        print("----------Composing Login Screen ---------------------------------")
        UserID = EntryLeaf(1)
        Password = EntryLeaf(2)
        SubmitButton = ButtonLeaf(1)
        LoginFrame.add(UserID)
        LoginFrame.add(Password)
        LoginFrame.add(SubmitButton)
        self.controller.onButtonClick(SubmitButton.operation())

        print("------------------End----------------------------------------")
        UserID.setEntryValue("Deepankar")
        Password.setEntryValue("123456")

    def profilePage(self):
        ProfileFrame =Composite()
        print("---------Composing Profile Screen-----------------------------")



    def VideoConferencePage(self):
        pass



if __name__ == "__main__":
    pass
   #main =App()
  #  main.loginPage()


