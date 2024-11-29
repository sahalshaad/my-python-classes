dict_var = {
    "name" : "sahal",
    "age" : 21,
    "place" : "calicut",
    "stydy" : "celiums"
}
print(dict_var["age"])
print(dict_var["name"])
print(len(dict_var))

print(type(dict_var))

sahal = ["latheef","22","calicut","celiums"]
keys = ["name","age","place","company"]
dictionary = dict(zip(keys, sahal))

# sahal_one = dict(sahal)
print(dictionary)

celiums = {
    "mender" : "hanna mam",
    "developers" : "varun sir, saleel sir, mansoor sir, sahal, basilka, abilashettan, aiswarya",
    "monjan" : "shabeeb",
    "bde" : "aneesha madam"
}

print(celiums.values())
print(celiums.keys())
print(celiums)
print(celiums.items())

celiums_list = list(celiums.items())
print(celiums_list)

celiums_tuples = tuple(celiums.items())
print(celiums_tuples)

celiums["color"] = "red, blue"
print(celiums)

celiums.update({"color" : "black"})
print(celiums)

celiums.pop("color")
print(celiums)

for x in celiums:
    print(x)
for x in celiums:
    print(celiums[x])

for x in celiums.values():
    print(x)

for x in celiums.keys():
    print(x)

for x, y in celiums.items():
    print(x, y)

#### copy dict ####

mydict = {"name":"sahalshad","place":"kuttiady","study":"calicut","number":7012596870,"cource":"python"}
"""mydict_copy = mydict.copy() #copy method
print(mydict_copy)"""
mydict_copy = dict(mydict)
print(mydict_copy)

### NESTED DICTIONARIE ###

my_family = {"member 1":{"latheef":"latheef@gmail.com","id":"2024"},
             "member 2":{"sabeera":"sabeera@gmail.com","id":"4076"},
             "member 3":{"sahal":"sahal@gmail.com","id":"6238"},
             "member 4":{"reema":"reema@gmail.com","id":"3476"},
             "member 5":{"rifa":"rifa@gmail.com","id":"6512"},}
print(my_family)

print(my_family["member 2"])
print(my_family["member 2"]["id"])

"""for x, obj in my_family.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])"""
for x, obj in my_family.items():
    print(x)
    for y in obj:
        print(y + ":",obj[y])

z = my_family.get("")
print(z)       

# python operators
d = 5
i = 7

#print(d + i)   #   
d += 4          #   = d = d+4 == 9
print(d)
#python arithmetic oprators
g = 5
u = 2
print(g,u)
print("addition" + str (g+u)) #addition

print("subtraction" + str (g-u)) #subtraction

print("division" + str(g/u)) #division

print("multiplication" + str(g*u)) #multiplication

print("modulus"+ str(g%u)) #modulus

print("Exponentiation"+str(g**u)) #Exponentiation

print("Floor division"+str(g//u)) #Floor division

#python assignment oprators

a = 7
print(a)

a +=4   #a = a + 3
print(a)

q=6
q -=3  #q = q-3
print(q)

w=4
w *=4  #w = w*4
print(w)

t=5
t/=5 #t=t/5
print(t)

y=6
y = 5
y **= 3
print(y)

x = 5
x &= 3
print(x)

