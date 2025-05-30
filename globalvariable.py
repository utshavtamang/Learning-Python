x = 'hello'
def myfunc():
    global x
    x = "Apple"
    print(x)
myfunc()

print(x)