thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#1
print(thisdict.get("model",None))
#2
x = 'not present'
for i in thisdict.keys():
    if i == "model":
        a = 'present'
print(x)
#3
print(len(thisdict))
#4
print(list(thisdict.keys()))
#5
print(list(thisdict.values()))
#6
thisdict2 = {
  "brands": "Ford",
  "models": "Mustang",
  "years": 1964
}
print(thisdict.update(thisdict2))
#7
print(thisdict.pop('models',None))
#8
print(thisdict.clear())
#9
if len(thisdict) == 0:
    print("Empty dictionary")
else:
    print("Not empty Dictionary")
#10
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "models": "Malibu",
  "year": 1964
}
for key in thisdict.keys():
    print(key, thisdict[key])
#11
a = input("Value:")
thisdict['model'] = a
print(thisdict['model'])
#12
print(list(thisdict.values()).count(a))
#13
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
new_dict ={}
for key, value in list(thisdict.items()):
    new_dict[value] = key
print(new_dict)
#14
target = input("Value:")
for key, value in thisdict.items():
    if value == target:
        print(key)
#15
keys = ['a','b','c','d']
values = [3,3,5,2]
new_dict = dict(zip(keys,values))
print(new_dict)