a =1 
b ='2'
c =3
print(int(2.5))#siempre tener todos los parentesis cerrados
print(a + float(b))#tener en cuenta el tipo de caracter 
#print (c/0)#error de diviison por 0
try:
    print(c/0)
except ZeroDivisionError: #solo se ejecuta con esta exeption
    print (0)

def divide(a,b):
    try:
        return a/b
    except:#se ejecuta cuando encuentra una exepcion
        return "Zero division is maningless"

print (divide(1,3))
print (divide(1,0))

