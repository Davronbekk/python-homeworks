set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
#1
print(set1.union(set2))
#2
print(set1.intersection(set2))
#3
print(set1.difference(set2))
#4
print(set1.issubset(set2))
#5
a = int(input("Enter Element"))
if a in set1:
    print(True)
else:
    print(False)
#6
print(len(set1))
#7
lst = [1,2,3,4,5,6,7,8,9]
new_set = set(lst)
print(f"{new_set} -> type:{type(new_set)}")
#8
a = int(input("Enter Element"))
set1.discard(a)
#9
print(set1.clear())
#10
if len(set1) == 0:
    print("Empty")
else:
    print("Not empty")
#11
set1 = {1, 2, 3, 4, 5}
print(set1.symmetric_difference(set2))
#12
set1.add(6)
#13
set1.pop(6)
#14
print(max(set1))
#15
print(min(set1))