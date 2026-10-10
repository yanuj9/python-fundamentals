# many forms

class Laptop:       #Duck
    def build(self):
        print("Laptop builds")

class Desktop:      #crow
    def build(self):
        print("Desktop builds")

class Alien:
    def code(self, machine : Laptop):
        print("Alien Building...")
        machine.build()

myLappy = Laptop()
beast = Desktop()

anuj = Alien()
# anuj.code(myLappy)
anuj.code(beast)