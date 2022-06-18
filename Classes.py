class Var:
    x = 5
p1 = Var
print(p1.x)

class Tao:
    def __int__(self, name, age):
        self.name = name
        self.age = age
p2 = Tao("Hello", 17)
print(p2)
print(p2.age)
print(p2.name)