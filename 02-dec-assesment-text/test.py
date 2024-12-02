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

