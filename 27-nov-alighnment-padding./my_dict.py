my_dict = {'key':'value','key2':'value2','key3':[32,'hii'],'key4':'value4'}
print(my_dict)
print(my_dict['key3'][0])

print(my_dict['key2'].upper())

d = {'key1':{'nestkey':{'subnestkey':'subnestvalue'}}}
print(d)
print(d['key1']['nestkey']['subnestkey'])

print(d.values)

t = (1,2,3,4,3)
print(type(t))
print(t)
print(t[0])
print(t.index(4)) #4 ithil ethra pravishym undenn ariyaan
print(t.count(3)) #ethra pravishyam 3 vannu

setx = set()
setx.add(44)                           #setill or value or pravishyamee varullu, so ath kond listil koree 
                                        #value orupole ullath undenkil athine set aakiyaal sheriyaayi kittum
setx.add('sahal')
setx.add('rashiq')
setx.add('rashiq')
print(setx)

kalapila = [1,1,1,3,3,2,2,5,6,7]
print(set(kalapila))

b = 1+2==6            #this is boolean
print(b)

g = None
print(g)