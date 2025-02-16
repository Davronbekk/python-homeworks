tup = (1,2,3,4,5,6)
#1
a = int(input("Enter a number: "))
print(tup.count(a))
#2
print(max(tup))
#3
print(min(tup))
#4
a = int(input("Enter a number: "))
print(a in tup)
#5
print(tup[0])
#6
print(tup[-1])
#7
print(len(tup))
#8
print(tup[:3])
#9
tup1 = (1,2,3,4,5,6)
tup2 = (8,9,10,11,12)
print(tup1 + tup2)
#10
if len(tup) == 0:
    print("Empty tuple")
#11
a = int(input("Enter a number: "))
for index, value in enumerate(tup):
    if value == a:
        print(f"index: {index}, value: {value}")
#12
new_tup = sorted(set(tup))
print(new_tup[-2])
#13
new_tup = sorted(set(tup))
print(new_tup[1])
#14
a = int(input("Enter a number: "))
new_tup = (a,)
if type(new_tup) is tuple:
    print("it is tuple")
else:
    print("no")
#15
lst = [1,2,3,4,5,6,7,8,9]
new_tup = tuple(lst)
print(f"{new_tup} -> type:{type(new_tup)}")