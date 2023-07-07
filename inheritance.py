class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A):  # Multilevel 
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


class C(B,A):  #Multiple inheritance
    def feature5(self):
        print("Feature 5 is working")

a1 = A()
a1.feature1()
a1.feature2()

b1 = B()

c1 = C()
c1.feature3()