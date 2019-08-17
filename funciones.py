def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

print(minutes_to_hours(60))

def minutes_to_hours2 (minutes, secons):
    hours = minutes / 60 + secons /3600
    return hours

def minutes (secons, minutes = 20):
    hours = minutes/60 + secons /3600
    return hours

print(minutes(20))
print (minutes(20, 40))#en este caso si sostitule el 20

def age_foo(age):
    new_age = float(age) +50
    return new_age

age = input("enter your age: ")
print (age_foo(age))
