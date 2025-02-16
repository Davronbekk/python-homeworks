a = round(float(input("Enter a number: ")),2)
b = round(float(input("Enter another number: ")),2)
print(a, b)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

largest = max(a, b, c)
smallest = min(a, b, c)
print(largest, smallest)

a = float(input("Enter a km: "))
meter = a * 1000
centimeters = a * 100000
print(meter, centimeters)

a = int(input("Enter a Celsius: "))
f = (a*(9/5)+32)
print(f)

a = int(input("Enter a num: "))
a = str(a)
print(a[-1])

a = int(input("Enter a num: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")