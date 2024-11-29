myList = ['one','two','three','four',655,6534.76,'six']
print(myList)
print(myList[2:4])

myList = myList+['seven']
print(myList)

myList*2
print(myList)

myList.append('appended me')
print(myList)

print(myList.pop(4))

list1 = ['hi','hlo','hy']
list2 = ['run','walk']
list3 = ['rain','water','mitty']

nested_list = [list1,list2,list3]
print(nested_list)

print(nested_list[0])
print(nested_list[0][0])

List_Comprehensions = [row[0] for row in nested_list] # nested listil illa itemsil oro itemsileeyum first item print avum...
print(List_Comprehensions) #['hi', 'run', 'rain']
