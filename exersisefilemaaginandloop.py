temperatures=[10,-20,-289,100]
def c_to_f(c):
    with open("/home/salem/Documents/04 universidad/05-python/megacurso/exampleExersise.txt", 'a') as file:     
        if c< -273.15:
            print (str(c)+" this not can be")
        else:
            f=c*9/5+32
            file.write(str(f)+"\n")

for t in temperatures:
    c_to_f(t)

with open("/home/salem/Documents/04 universidad/05-python/megacurso/exampleExersise.txt", 'r') as file:
    content = file.read()
    print (content)


