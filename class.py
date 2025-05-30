class abc:
    x = 5
yut = abc()
print(abc.x)
class car:
  def __init__(xyz, brand, color):
    xyz.brand = brand
    xyz.color = color

p1 = car("Honda", "Red")

print(p1.brand)
print(p1.color)
class hello:
  def _init_(tyu, name, age):
    tyu.name = name
    tyu.age = age
  def _str_(tyu):
    return f"{tyu.name} and {tyu.age}"
  a = ("Ram", 18)
  print(a)
class Person:
  def __init__(ssg, name):
    ssg.name = name
    
  def myfunc(ssg):
    print("Hello I am " + ssg.name)

class man:
  def __init__(tyu, he, jo):
    tyu.f = he
    tyu.l = jo
  def fon(tyu):
    print(tyu.f, tyu.l)
a = man("Utshav", "Tamang")
a.fon()
