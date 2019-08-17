fileRead = open("/home/salem/Documents/04 universidad/05-python/megacurso/example.txt", 'r')
content2 = fileRead.readlines()
content2 = [i.rstrip("\n") for i in content2]
for item in content2:
    print (str(len(item)))


print(content2)
print(type(content2))


#eliminamos \n de la lista 
print(content2)

fileRead.close
fileRead = open("/home/salem/Documents/04 universidad/05-python/megacurso/example.txt", 'a')
fileRead.write("another line")
