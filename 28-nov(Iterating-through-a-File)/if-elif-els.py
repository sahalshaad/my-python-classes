x = False
if x:
    print('i was true')
else:
    print('I will be printed in any case where x is not true')

c = 10<20
if c is True:
    print('c is true')
else:
    print('c is not true')

# t = {'name':'sahal','address':'parappummal'}
# if t['name']=='sahal':
#     print("My name is ",t['name'],"\n My address is ",t['address'])

f = {'place':'calicut','number':7012596870}
if f['place']=='calicut':
    print('place is',f['place'])
else:
    print("place don't know")

p = 65+5==70
u = 70+8==78
if p is False:
    print('true')
elif u is True:
    print('u is true')
else:
    print('u is fauls')

y = "black"
if y=="white":
    print('inn dosha')
elif y=="b":
    print('inn nalla dam biriyani')
else:
    print('inn food illa')

list11 = [1,2,3,4,5,6,7,8,9,0]
for num in list11:
    print(num)

list12 = ['sahal','anas','ajnas','minhaj']
for names in list12:
    print(names)


animals = ['fox','dog','cat','cow']
for anmi in animals:
    print('i like', anmi)

for i in range(1, 11):  # Numbers from 1 to 10
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

for ii in range(11,31):
    if ii % 2 ==0:
        print(f"{ii} is even")
    else:
        print(f"{ii} is odd")
print(19/6)
print(19 % 6)

list32 = [1,2,3,4,5,6,7,8,9,10]
for num in list32:

    if num % 2==0:
        print('num is even')
        new=[]
        new=new.append(num%2==0)
        print(num)
    else:
        print('number is odd')
        nw=[]
        nw=nw.append(num%2!=0)
        print(num)

user = int(input('enter a number:'))
if user % 2 == 0:
    print('number is even')
else:
    print('number is odd')



