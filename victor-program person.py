class Person(object):
    def work(self):
        print("%s goes to work" % self.name)

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, job, payday):
        super(Employee, self).__init__()
        self.Job = job
        self.Money = payday

    def Job(self):
        print("You work at Wendy's")

    def Payday(self):
        print("You are getting pay 200 dollars")


class Programer(Employee):
    def __init__(self, Computer):
        super(Programer, self).__init__(Computer)
        self.Computer = Computer

    def Computer(self):
        print("You are working on a program")
