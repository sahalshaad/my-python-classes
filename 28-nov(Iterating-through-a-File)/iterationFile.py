# f = open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/pythontext.txt","r")
f = open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/pythontext.txt","w+")
f.write("first wrotr")
print(f.seek(1))
print(f.read())
f = open("/Users/sahal/Documents/vs code/Html/Ceiliums Tech Class/pythondemo/pythontext.txt","a+")
f.write("\nmy append text")
f.write('\nsecond append text')
f.seek(0)
print(f.read())

f.close()
# for x in f:
#     print(x)