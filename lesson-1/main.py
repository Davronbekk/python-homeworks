hello = r"Hello \n\tWorld"
a = r"str(input(\"Write smth:\"))"
print(f"hello {a}fdaf")
print("fjfjf {a} {hello}".format(a=a,hello=hello))
print("{} {}".format(a, hello))

n = 23.23232
z =23.23
print(f"{z:<8} - numbers")
print(f"{n:.5f} - numbers")

print(len(a))
word = input()
print(word[-1])
print(a[::-1], word, sep=" ")