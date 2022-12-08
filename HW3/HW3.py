file = open("data","w")
file.write("Name: Super\nSurname: Can\nGender: Male\nUsername: TTkid\nJob: Lumberjack")
file.close()

file = open("data")
text = file.read()
list = text.split()
for i in range(0,len(list)-1):
    for j in list[i]:
            list[i] = list[i].replace(':','')
mydic = {list[i]:list[i+1] for i in range(0,len(list)-1,2)}
print(mydic,type(mydic))
file.close()