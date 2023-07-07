class Student:

    school = "BCIIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def add():
        return 3 + 4

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

s1 = Student(54,45,21)
print(s1.avg())
print(Student.getSchool())
print(Student.add())