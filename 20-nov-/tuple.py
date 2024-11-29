tuplevar = ('fg','bn','po','uy','tu')
tuplevar2 = ('54','76','pwo87','74ury','tu66p')
print(type(tuplevar))
print(type(tuplevar2))
print(tuplevar)
print(tuplevar2)
listvartuple = list(tuplevar)
print(listvartuple)
listvartuple[3]="sahal"
print(listvartuple)
tuplevar = tuple(listvartuple)
print(tuplevar)

#******** using append ********
tuplevarappend = ('boottle','water','dringing','eating')
y = list(tuplevarappend)
y.append('apple')
print(y)
tuplevarappend = tuple(y)
print(tuplevarappend)

#*******  add tuple to a tuple  *******
p = ('tv','fridge','mixi')
o = ('mashing machine','ythytfgtrf','infinity item you can add')
p += o
print(p) 

# Unpacking a tuple:

ty = ('qween','lion','king','zeebra')
(gold, yello, diamond, forest) = ty
print(gold)

# method 2********
tyt = ('qween','lion','king','zeebra','cat','hilite','park','seaview')
(gold, yello, diamond, *forest) = tyt
print(gold)
print(forest)

# for loop in tuple
thistuple = ('stuv','opqr','klmn','hig','efg','abcd')
for i in thistuple:
    print(i)

# for loop with range length*****
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


    