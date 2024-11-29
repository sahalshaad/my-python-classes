sets_one = {"one","two","three","four"} # set variable create
print(sets_one) # print sets item
print(type(sets_one)) # print which type variable

#converting sets to list
convert_to_list = list(sets_one)
print(convert_to_list)

#changing the items in list
convert_to_list[2] = "tow,two" #change the value of index 2 
print(convert_to_list) # value changed sucessfully

# appending new item
convert_to_list.append("five") #appending new item
print(convert_to_list) #appended successfully

# converting list to set
sets_one = set(convert_to_list)
print(sets_one) 

# another method for adding new item
sets_one.add("six")
print(sets_one)

# remove item in the set
# sets_one.remove("one")
print(sets_one)

# update set
sets_two = {"yellow","blue","black"}

sets_one.update(sets_two)
print(sets_two)
# for loop on sets
for x in sets_one:
    print(x)

# Join Sets
sets_three = sets_one.union(sets_two)
print(sets_three)

sets_four = sets_one | sets_two
print(sets_four)

sets_five = {"brown","blackberry","bluberry","stroberry","suger"}
sets_six = {"water","sea","waterfalls","fish","boat","ship","suger"}
all_sets = sets_one.union(sets_two, sets_six, sets_five)

print(all_sets)

intersectionvar = sets_five.intersection(sets_six)
print(intersectionvar)

sets_seven = sets_five.symmetric_difference(sets_six)
print(sets_seven)

sets_five.difference_update(sets_six)
print(sets_five)

sets_eight = sets_five ^ sets_six
print(sets_eight)
