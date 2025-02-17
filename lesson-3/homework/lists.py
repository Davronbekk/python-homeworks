lst = [1,2,3,4,5,6,7,8,9]
#1
element = int(input("Enter the element to count: "))
count = lst.count(element)
print(f"The element '{element}' appears {count} time(s) in the list.")
#2
print(sum(lst))
#3
max_value = max(lst)
print(max_value)
#4
min_value = min(lst)
print(min_value)
#5
a = int(input("Enter the number to check: "))
if a in lst:
    print(f"The element '{element}' is in the list.")
else:
    print(f"The element '{element}' is not in the list.")
#6
if lst:
    print(f"The first element: {lst[0]}")
else:
    print("The list is empty.")
#7
if lst:
    print(f"The first element: {lst[-1]}")
else:
    print("The list is empty.")
#8
first_three = lst[:3]
print(f"The first three elements: {first_three}")
#9
reversed_lst = lst[::-1]
print(f"The reverse list: {reversed_lst}")
#10
lst_e = [2,4,6,3,1,9,5]
sorted_l = sorted(lst_e)
print(f"The sorted list: {sorted_l}")
#11
list(set(lst_e))
print(f"duplicated removed: {lst_e}")
#12
a = int(input("Enter: "))
index = int(input("index to insert at: "))
lst_e.insert(index, a)
print(f"Updated list: {lst_e}")
#13
a = int(input("Enter the element to find: "))
if a in lst_e:
    index = lst_e.index(a)
    print(f"The first occurrence of '{a}' is at index: {index}")
else:
    print(f"The element '{a}' is not in the list.")
#14
print(f"Is the list empty? {len(lst_e) == 0}")
#15
counter = 0
for num in lst_e:
    if num % 2 == 0:
        counter += 1
print(f"{counter} elements are even.")
#16
counter = 0
for num in lst_e:
    if num % 2 != 0:
        counter += 1
print(f"{counter} elements are odd.")
#17
concatenated_list = lst + lst_e
print(f"The concatenated list: {concatenated_list}")
#18
sublist = [6,3,1]
result = False
for x in range(len(lst_e) - len(sublist)+ 1):
    if lst_e[x:x+len(sublist)] == sublist:
        result = True
        break
print(f"Does the sublist exist?{result}")
#19
old = int(input("Enter the element to replace: "))
new = int(input("Enter the new element: "))
if old in lst:
    index = lst.index(old)
    lst[index] = new
    print(f"Updated list: {lst}")
else:
    print(f"The element '{old}' is not in the list.")
#20
new_lst = list(set(lst))
new_lst.sort()
print(f"The second largest element is:{new_lst[-2]}")
#21
new_lst = list(set(lst))
new_lst.sort()
print(f"The second largest element is:{new_lst[1]}")