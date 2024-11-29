# print(list(range(0,21,2)))

# index_count = 0
# for letter in 'abcdefghigklmnopqrstuvwxyz':
#     print('At index {} the letter is {}'.format(index_count,letter))
#     index_count += 1

# for i,letter in enumerate ('abcdef'):
#     print('At index {} the letter is {}'.format(i,letter))

# enumerate

# fruits = ['apple', 'banana', 'cherry']

# for index, fruit in enumerate(fruits):
#     print(f'Index {index} contains {fruit}')

# print this ******

# Index 1 contains apple
# Index 2 contains banana
# Index 3 contains cherry

# fruits = ['apple','banana','cherry']
# for inx, fruits in enumerate(fruits, start=1):
#     print(f'index {inx} Contains {fruits}')

# print this ************
# 0. Name
# print 10 names
# code in *#*#*#*#*#*#*#*#*#*#

# names = ['Name','Sahal','Shabeeb','Anas','Ajnas','Minhaj','Rashiq','Saleel','Mansoor','Varun']
# for counts, names in enumerate(names):
#     print(f'{counts} {names}')

# itext = 'hello'
# for inx, itext in enumerate(itext, start=1):
#     print(f'{inx} {itext}')

# print(list(enumerate('abcde', start=1)))

# zip() ********
ziplist1 = ['sahal','anas','irfan','afnan']
ziplist2 = ['macbook','dell','hp','azuz']

# zip(ziplist1,ziplist2)
# print(zip())

for item1, item2 in zip(ziplist1,ziplist2):
    print('my name is  {} and i am using {}'.format(item1,item2))

print('a' in ['x','y','z'])
