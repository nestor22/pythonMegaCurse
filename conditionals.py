a= 3
if a < 5:
    print("less than  5")
elif a == 5 :
    print("equal to 5")
else:
    print ("greter than 5")

def age_foo(age):
    new_age = age+ 50
    return new_age

age = int(input("enter you age: "))

if age < 150:
    print(age_foo(age))
else:
    print("how is that possible?")
