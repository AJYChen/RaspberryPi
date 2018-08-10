z = input("Please enter 1 for true or 2 for false(q to quit):")
m = bool()

while z != "q":
    if z == 1:
        m = True
    elif z == 2:
        m = False
    else:
        break
    
    
while m == True:
        a = input("String to capitalize [q to quit]")
        if a == "q":
            break
        else:
            print(a.capitalize())

while m == False:
    q = input("Integer, please [q to quit]")
    if q == "q":
        break
    q = int(q)
    if q % 2 == 0:
        continue
    else:
        w = q*q
        print(q,"squared is",w)
