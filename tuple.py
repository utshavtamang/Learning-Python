tuple1 = ("Ram", "Shyam", "Hari")
x = ("Gopal", "krishna")
tuple1 += x
print(tuple1)
y = list(tuple1)
y.append("ramesh")
tuple1 = tuple(y)
print(tuple1)
(a, b, *c) = tuple1
print(a)
print(b)
print(c)
tuple2 = tuple1*2
print(tuple2)