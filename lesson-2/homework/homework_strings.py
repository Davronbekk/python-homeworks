#1
a = input("Name:")
b = int(input("Year of Birth:"))

print(2025-b)
#2
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])
#3
a = input("Enter String:")
print(len(a))
a.upper()
a.lower()
#4
if a == a[::-1]:
    print("Palindrome",True)
else:
    print("Palindrome",False)
#5
a = input("Enter String:")
vowels_chars = ['a', 'e', 'i', 'o', 'u']
vowels = 0
consonants = 0

for char in a:
    if char.isalpha():
        if char in vowels_chars:
            vowels += 1
        else:
            consonants += 1
print(vowels, consonants)
#6
a = input("Enter String:")
b = input("Enter String:")
print(b in a)

#7
a = input("Enter Sentence:")
b = input("Replace:")
c = input("With:")
a = a.split(' ')
for word in a:
    if word == b:
        print(c, end=" ")
    else:
        print(word, end=" ")

#8
a = input("Enter Sentence:")
print(a[0], a[-1])
#9
a = input("Enter Sentence:")
print(a[::-1])
#10
a = input("Enter Sentence:")
print(len(a.split(' ')))
11
a = input("Enter Sentence:")
b = False
for char in a.split(' '):
    if char.isdigit():
        b = True
print(b)
#12
a = input("Enter Words:").split(' ')
separator = '-'
joined_str = separator.join(a)
print(joined_str)
#13
a = input("Enter Sentence:")
print(a.replace(' ',''))
#14
a = input("Enter Sentence:")
b = input("Enter Sentence:")
if a == b:
    print("Equal")
else:
    print("Not Equal")
#15
a = input("Enter Sentence:")
acronym = ''
for acron in a.split():
    acronym += acron[0].upper()
print(acronym)
#16
a = input("Enter Sentence:")
b = input("Enter character:")
print(a.replace(b,''))

#17
a = input("Enter Sentence:")
vowels = ['a', 'e', 'i', 'o', 'u']
for char in vowels:
    if(char in a):
        a = a.replace(char,'')
print(a)

#18
a = input("Enter Sentence:").split()
print("Start with:",a[0])
print("End with:",a[-1])

