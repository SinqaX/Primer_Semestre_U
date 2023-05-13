n1 = int(input("agregar n1"))
n2 = int(input("agregar n2"))
n3 = int(input("agregar n3"))

if n1>n2:
    if n2>n3:
        print("orden ascendente", n3, n2, n1)
    else:
        if n1>n3:
            print("ordewn ascendente", n2, n3, n1)
        else:
            print("orden ascendente", n2, n1, n3)
else:
    if n1>n3:
        print("orden ascendente", n3, n1, n2)
    else:
        if n2>n3:
            print("orden ascendente", n1, n3, n2)
        else:
            print("orden ascendente ", n1, n2, n3)
            

          