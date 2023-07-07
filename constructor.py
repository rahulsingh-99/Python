class Person:
    name = "Rahul"
    age = 22

    def __init__(self, n, a):
        print("Hello World")
        self.name = n
        self.age = a

    def info(self):
        print(f"{self.name} and his age is {self.age}")


detail = Person("Johnny", 38)
detail1 = Person("Blake", 21)
detail2 = Person("Kenzie", 26, "Model")
detail.info()
detail1.info()
detail2.info()
