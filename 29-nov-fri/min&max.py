minmax = [65,74,43,98,65,987,78,90]
print(min(minmax))
print(max(minmax))
minmax.sort()
print(minmax)
print("-------------------------------------------")
from random import randint
print(randint(1000,2000))

# inputarray = input('enter somthing in the box: ')

# print(inputarray)

print("-------------------------------------------")

listco = [x for x in 'word''work''walk''wide']
print(listco)

print("-------------------------------------------")

rangelist = [x for x in range(15) if x % 2 == 0]
print(rangelist)

st = ['string', 'simbs', 'sonu', 'santhosh', 'santheep', 'saambar']
for word in st.split():
    if word[0] == 's':
        print(word)
