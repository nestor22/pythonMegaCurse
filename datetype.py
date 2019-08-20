r"""
This a class of day 6 for date
how fomat day and another thigs like that
"""
import datetime

print(datetime.datetime.now())
now = datetime.datetime.now()
yesterday = datetime.datetime(2016, 11, 11,0,48,0)
print(now)
print(yesterday)
#formatos para las fechas
now.strftime("%Y-%m-%d-%H-%s-%f")
print(now.strftime("%Y-%m-%d-%H-%s-%f"))
now.strftime("%B %Y %d")
print(now.strftime("%B %Y %d"))
#agregar fechas 
print(yesterday = now + datetime.timedelta(days=2))
print(yesterday = now + datetime.timedelta(seconds=2))

"""
this script create an empy file
"""

filename = datetime.datetime.now()

def create_file():
    """This fuccnion create an empy file"""
    with open(filename.strftime("%Y-%B-%d-%H"),'w') as file:
        file.write("") #empty string
create_file()
