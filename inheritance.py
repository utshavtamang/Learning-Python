class animal:
    def sleep(self):
        print("This animal sleeps")
    def eat(self):
        print("This animal eats")
class tiger(animal):
    pass
Tiger = tiger()
Tiger.eat()
tuple1 = ("ram", "Shyam", "Hari")
for z in tuple1:
    print(z)
x = iter(tuple1)
print(next(x))
print(next(x))
print(next(x))
stri = "Ram"
y = iter(stri)
print(next(y))
print(next(y))
print(next(y))
