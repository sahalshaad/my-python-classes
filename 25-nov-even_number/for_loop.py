### nested for loop
print("nested for loop")

nestedlist1=['big','small','medium']
nestedlist=['apple','banana','cherry']
for x in nestedlist:
 for y in nestedlist1:
    print(x,y)
### range with for loop
print("range with for loop")
for x in range(8):
  print(x)

### for x in range(2, 6):
print("for x in range(, 6)")
for x in range (10,51):
  print(x)

### change the default value of sequecne
print("increment the sequence by 3")
for x in range (-1,20,2):
  print(x)

### for loop with last print using else
print("for loop with last print using else")
for x in range (1,8):
  print(x)
else:
  print("finelly finished")
  