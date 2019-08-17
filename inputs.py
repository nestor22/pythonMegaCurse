def currecy_converter(rate, eruros):
    dollars = eruros*rate
    return dollars
r=float(input('Enter the rate: '))
e=float(input('Enter the euros: '))
print(str(currecy_converter(r,e)))

