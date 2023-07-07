class Person:

    def __init__(self, name, age, address):
        self.__name = name  #!private
        self._age = age     #! protected
        self.address = address #!public
    
    def __displayName(self):
        print("Name =", self.__name)

P = Person("Rahul", 22, "Delhi")
print("Address =",P.address)
print("Age =",P._age)
P._Person__displayName()