class Var:
    x = 5
p1 = Var
print(p1.x)

class Tao:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Greet(self):
        print("Hello my name is {}, aged {} years old".format(self.name,self.age))


p2 = Tao("Hello", 17)
print(p2)
print(p2.age)
print(p2.name)
p2.Greet()