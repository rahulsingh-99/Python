class Person:

    def __init__(self, name, age, address):
        self.__name = name  #!private
        self._age = age     #! protected
        self.address = address #!public
    
    def displayName(self):
        print("Name =", self.__name)

P = Person("Rahul", 22, "Delhi")
print("Address =",P.address)
print("Age =",P._age)
P.displayName()
#P._Person__displayName() #! this is for displaying private method but not recommend anyone for this