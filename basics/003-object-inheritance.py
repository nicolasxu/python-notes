
class People():
    def __init__(self,name=""):
        self.name = name

    def say_hi(self):
        print(self.name + ' hi!')

class Employee(People):
    def __init__(self,name="", employee_id="",):
        super().__init__(name)
        self.employee_id = employee_id

    def say_hi(self):
        print("{}({}) says hi!".format( self.name, self.employee_id ))

p1 = People('nick')
p2 = People('john')
e1 = Employee('Lucy', "113")
p1.say_hi()
p2.say_hi()
e1.say_hi()