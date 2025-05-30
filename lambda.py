x = lambda a, b : a * b
print(x(2, 5))
def abc(n):
    return lambda a: a * n
a = abc(1)
y = abc(2)
z = abc(3)
print(a(11))
print(y(11))
print(z(11))