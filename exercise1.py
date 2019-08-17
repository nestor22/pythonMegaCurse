def convertCelsiusToFahremheit(degress):
    f = degress * 9/5 +32
    return f

try:
    celsius = float(input("plis input the celsius degress: "))
    if celsius <= -273.15:
        print("thas is imposible")
    else:
        print ("fharenheis is: " + str(convertCelsiusToFahremheit(celsius)))
except:
   print("eror you dont put a number of degress")
   
