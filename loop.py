
i = 0
while i < 6:
    if i == 5:
        break
    print(i)
    i += 1
i = 1
while i < 7:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print("i is not less than 7 now")
x = ["apple", "banana", "mango"]
for y in x:
    if y == "banana":
        break
    print(y)
lis = ["ram", "shyam", "hari"]
for x in lis:
    if x == "shyam":
        continue
    print(x)
abc = ["bone", "heart", "lungs", "liver"]
for x in abc:
    print(x)
else:
    print("Loop is finished")
for x in range(2):
    print(x)