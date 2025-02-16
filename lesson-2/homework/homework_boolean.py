#1
a = input("Enter a Username: ")
b = input("Enter a Password: ")
if a and b:
    print(True)
else:
    print(False)

#2
a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
if a and b:
    print("Equal")
    print(True)
#3
a = int(input("Enter a num: "))
if a > 0 and a % 2 ==0:
    print("positive and even")
    print(True)
#4
a = int(input("Enter a num: "))
b = int(input("Enter a num: "))
c = int(input("Enter a num: "))

if a!=b and b!=c and c!=a:
    print("Are they different?", True)
else:
    print("Are they different?", False)

#5
a = input("Enter a Sentence: ")
b = input("Enter a Sentence: ")
if len(a) == len(b):
    print('They have same length')
#6
a = int(input("Enter a num: "))
if a % 3 == 0 and a % 5 == 0:
    print("it can be divided by 3 and 5")
#7
a = float(input("Enter a num: "))
b = float(input("Enter a num: "))
if a+b > 50.8:
    print("Sum is bigger than 50.8")
#8
a = int(input("Enter a num: "))
if a >= 10 and a <= 20:
    print("Between 10 and 20")
    print(True)
else:
    print("NotBetween 10 and 20")
    print(False)
