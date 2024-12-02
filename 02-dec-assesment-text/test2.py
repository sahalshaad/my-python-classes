st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word [0]=='s':
        print(word)

lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has"
for loremword in lorem.split():
    if loremword [0]=='s':
        print(loremword)

name = "Alice"
age = 30
print("Name:", name, "Age:", age)

print('hi','hello', sep=' & ')
print('26','04','2003',sep='-')

print('sahal','shad',end=' pa\n',sep='')

amount = 44534.85
print(amount)
print(type(amount))
print('amount : ${:.2f}'.format(amount))

name = 'sahal'
age = 21
place = 'calicut'
study = 'Celiums Tech'
home = 'kunduthode'

print(f'my name is {name}. i am {age} years old. i currently living in {place}, and studying at {study}. my home in {home}')

# userinput = int(input('enter a number'))
# sum = userinput + 5
# print('the sum is %d'%sum)

xx, yy = input("enter 2 numbers").split()

# xx = int(xx)
# yy = int(yy)
print("numbers of boys:", xx)
print("number of girls:", yy)

