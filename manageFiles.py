fileRead = open("/home/salem/Documents/04 universidad/05-python/megacurso/example.txt", 'r')
content = fileRead.read()
#esta linea lee todo el archivo y luego deja el puntero al fina
print(content)


print(type(content))
fileRead.seek(0)
#devuelve el puntero al inicio 
content2 = fileRead.readlines()
print(content2)
print(type(content2))

content2 = [i.rstrip("\n") for i in content2]
#eliminamos \n de la lista 
print(content2)

fileRead.close


with open("/home/salem/Documents/04 universidad/05-python/megacurso/example.txt", 'a+') as file:
    file.seek(0)
    content = file.read()
    file.write("\nLine 6")


print(content)