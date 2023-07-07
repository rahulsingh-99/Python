class Person:
    name = "Johnny"
    occupation = "CornStar"
    networth = 15000

    def info(self):
        print(f"{self.name} is a {self.occupation}")


details = Person()
details1 = Person()
details2 = Person()

details.name = "Blake"
details.occupation = "Model"

details1.name = "Ken"
details1.occupation = "Owner"

details2.name = "Kenzie"
details2.occupation = "Dancer"

details.info()
details1.info()
details2.info()
