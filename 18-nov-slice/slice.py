f="sahal, irfan, anas, shabeeb,"
print(f[0:5])
print(type(f))
print(f[:8])
print(f[:9])
print(f[:0])
print(f[-3:-6])
print(f.upper())
print(f.lower())
print(f.center(7))
print(f.capitalize())
a = " Hello, World! "
print(a.strip())

w=["sahal","fayis"]
print(len(w))

fh=("apple", "banana", "cherry")
list33=list(fh)
print(list33)

list1=list(("apple", "banana", "cherry"))
print("without variable",list1)

list222=["64534","hfgsfs","ytre45ref"]
print(list222[1:3])

print(list222[-2])

re=532
fd=635

if re>fd:
    print("'re' is greater than'fd'")
elif re<fd:
    print("'fd' is greater than're'")

print(bool(28<=29))

fruits=["apple","banana","orang","grapes","Pineapple"]
new=fruits[3]="mango"
print(fruits)
new1=fruits[3:]="munthiri","baththakka"
print(fruits)
fruits.insert(0,"stroberry")
print(fruits)
fruits.append("blackberry")
print(fruits)
animals=["kurkkan","patti","poocha"]
animals.extend(fruits)
print(animals)

animals.remove("patti")
print(animals)

new=fruits.pop(0)
print(new)



fruitss=['grapes','orange']

fruitss.clear()
print(fruitss)

fruitss.append("apple")
print(fruitss)

bottle=['7up','pepsi','meronda']
