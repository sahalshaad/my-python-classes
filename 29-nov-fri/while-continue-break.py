x = 0
while x < 10:
    print('x is currently',x)
    print('x is still less than 10, adding 1 to x')
    x += 1
    if x==3:
        print('x==3')
    else:
        print('continue..')
        continue

y = 0
while y < 10:
    print('y is currently',y)
    print('y is still less than 10, adding 1 to x')
    y += 1
    if y==4:
        print('y==4')
        break
    else:
        print('continue')
        continue

