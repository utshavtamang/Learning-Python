import re
qwe = "I am Utshav"
x = re.search("^I.*Utshav$", qwe)
if x:
    print("Yes")
else:
    print("No")
lio = "Brain rain main"
y = re.findall("dai", lio)
if y:
    print("Yes")
else:
    print("No")
tyu = "Hello the rain in spain up level"
z = re.search("the", tyu)
print(z.span())
d = re.split("\s", tyu, 3)
print(d)
e = re.sub("a","e", tyu, 1)
print(e)
h = re.search("in", tyu)
print(h.string)
j = re.search("spain", tyu)
print(j.group())