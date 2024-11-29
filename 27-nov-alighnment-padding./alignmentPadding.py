print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))


print('{0:^9} | {1:^14} | {2:^10} | {3:.^10} |'.format('Name','Address','Place','phone'))
print('{0:9} | {1:14} | {2:10} | {3:^10} |'.format('Sahal','Parappummal','Kuttiady','7012596870'))
print('{0:9} | {1:14} | {2:9} | {3:^10} |'.format('Ajnas','Non','Malappuram','436576983'))
print('{0:9} | {1:14} | {2:9} | {3:^10} |'.format('Shabeeb','Non','Malappuram','8755329976'))


name = 'sahal'
print(f'my name is {name}') # my name is sahal
print(f'my name is {name!r}') # my name is 'sahal'


num = 99999999.999
print('account balance is {0:10.6f}'.format(num))
print(num)
print(f"my name is {name!r}, my account balance:{num:10,.6f}")
# print(f"my name is {name!r}, my account balance:{num:{10}.{6}}")

print(f"my name is {name!r} my account balance:{num:{10}.{6}}")
# num = 23.45678
# print("My 10 character, four decimal number is:{0:10.4f}".format(num))
