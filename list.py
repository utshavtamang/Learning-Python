list = ["ram", "shyam", "hari", "sita", "gopal"]
list[1] = "Gita"
print(list)
list.insert(1, "Shyam")
print(list)
list.append("ramesh")
print(list)
abc = ["apple", "orange", "banana"]
list.extend(abc)
print(list)
a = []
for x in list:
    if "m" in x:
     a.append(x)
print(a)
b = [y.upper() for y in list]
print(b)
list.sort()
print(list)
list2 = list.copy()
print(list2)
List1 = ["apple", "orange", "banana"]
List2 = ["mango", "guava", "melon"]
list3 = List1 + List2
print(list3)