from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def processor(self):
        pass


class Laptop(Computer):
    def processor(self):
        print("It's running")


class Whiteboard():
    def write(self):
        print("Writing Code")


class Programmer:
    def work(self,lap):
        print("Solving Bugs")
        lap.processor()



# com = Computer()
# com.processor()

lap = Laptop()
board = Whiteboard()
pro = Programmer()
pro.work(lap)