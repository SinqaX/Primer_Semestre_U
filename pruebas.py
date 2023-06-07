resp=input("desea procesar triangulos ? (s/n) : ")
while resp=='s'or resp=='S':
    a=int(input("ingrese el valor a : "))
    b=int(input("ingrese el valor b : "))
    c=int(input("ingrese el valor c : "))
    if a>0 and b>0 and c>0:
        if a==b:
            if b==c:
                print("triangulo equilatero")
            else:
                print("triangulo isoceles")
        else:
            if a==c:
                print("triangulo isoceles")
            else:
                if b==c:
                    print("triangulo isoceles")
                else:
                    print("triangulo escaleno")
    resp=input("desea procesar triangulos ? (s/n) : ")


    

