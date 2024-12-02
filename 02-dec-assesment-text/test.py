st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word [0]=='s':
        print(word)

for num in range(0,11,2):
    print(num)


dividedby3 = [num for num in range(1,51)if num % 3 ==0]
print(dividedby3)

st = 'Go through the string below and if the length of a word is even print "even!"'

# Split the string into words and iterate through them
for word in st.split():
    # Check if the length of the word is even
    if len(word) % 2 == 0:
        print(f'{word} - even!')


myWords = 'Print every word in this sentence that has an even number of letters'
for wordin in myWords.split():
    if len(wordin) %2==0:
        print(f'{wordin} - even!*!')
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of
# five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1, 101):
    # Check for multiples of both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check for multiples of 3
    elif num % 3 == 0:
        print("Fizz")
    # Check for multiples of 5
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


for numb in range(1,101):
    # print(numb)
    if numb % 3 ==0 and numb % 5 ==0:
        print('fiz3buzz5')
    elif numb % 3==0:
        print('buzz')
    elif numb % 5 ==0:
        print('fizz')
    else:
        print(numb)
