#pendiente de colocar validacion para los float
def log_of_strig(string):
    return len(string)

def is_stirng(string):
    try:
#        if :
        int(string)
        return False
#        else:
 #           return True
    except:
        return True

string = input("type something: ")
if is_stirng(string):
    print(log_of_strig(string))
else:
    print("is no a string the numbers no have leng")

