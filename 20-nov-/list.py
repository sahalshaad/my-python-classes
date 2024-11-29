listrows = ['item1','item2','item3','item4','item5']
if "item3" in listrows:
    print("yes item3 in this listrows")
listrows[4] = "new_item"
print(listrows)

list2 = ['apple','blackberry','orange','watermelon','cherry','banana']
list2.sort()
print(list2)

# sort
numbers = ['10','54','76','32','11','24','87']
print(numbers)
numbers.sort()
print(numbers)

list2.sort(reverse=True)
print(list2)

numbers.sort(reverse=True)
print(numbers)

# copy method
list3 = ['disiplin','pray','food','oxigen','earth','water']
copylist3 = list3.copy()
print(copylist3)

# list method
list4 = ['cable','speaker','keybord','mouse','monitor','laptop']
print(list4)
listlistmethod = list(list4)
print(listlistmethod)

# slice operator
list5 = ['apple','blackberry','orange','watermelon','cherry','banana']
myslicelist = list5[:]
print(myslicelist)

# join method
numbersjoin = ['10','54','76','32','11','24','87']
listrowsjoin = ['item1','item2','item3','item4','item5']
join_num_li = numbersjoin + listrowsjoin
print(join_num_li)

# join ''for' loop' for append
forjoin = ['df','dd','cf','rd','tc','hs','kl']
forjoin2 = ['00','83','09','12','33','74','87','54']
for x in forjoin2:
    forjoin.append(x)
print(forjoin)