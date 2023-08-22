
def punto1():   
    print("\n1. se tiene una cantidad de numeros dad, determinar el primo mayor, "
          "el fibonacci menor,el par menor y realizar la multiplicacion con sumas\n") 
    cd=int(input("ingrese la cantidad de datos : "))
    z=0
    x=0
    c=0
    for i in range(cd):
        num=int(input("ingrese el numero "))
        r=2
        p=False
        while r<num and p==False:
            if num%r==0:
                p=True
            r+=1
        if p==False:
            if z==0:
                prma=num
                z=1
            else:
                if num>prma:
                    prma=num
        if num%2==0:
            if x==0:
                pame=num
                x=1
            else:
                if num<pame:
                    pame=num
        a=0
        b=1
        t=0
        while t<num:
            t=a+b
            a=b
            b=t
        if t==num:
            if c==0:
                fme=num
                c=1
            else:
                if num<fme:
                    fme=num
    co=1
    r=0
    while co<=prma:
        r+=pame
        co+=1
    rf=0
    co=1
    while co<=fme:
        rf+=r
        co+=1
    return  print(f"la multiplicacion de {prma} con {pame} y {fme} da como resultado : {rf}\n")



 
def punto2():
    print("\n2. se tiene una cantidad de numeros dada donde hay varios numeros que se reputen encotnrar"
           "el numero de veces que se repite el segundo fibonacci (en orden de entrada)y determinar si "
           "este contador es un numero primo\n") 
    cd=int(input("ingrese la cantidad de datos : "))
    cf=0
    c=0
    for i in range(cd):
        num=int(input("ingrese el numero : "))
        a=0
        b=1
        t=0
        while t<num:
            t=a+b
            a=b
            b=t
        if t==num:
            cf+=1
            if cf==1:
                pf=num
            elif cf==2:
                sf=num
                if pf==sf:
                    c+=1
            if sf==num:
                c+=1
    r=2
    p=False
    while r<c and p==False:
        if c%r==0:
            p=True
        r+=1
    if p==False:
        return  print(f"el contador={c} de las veces que se repite el segundo fibonacci es primo\n")
    else:
        return  print(f"el contador {c} de las veces que se repite el segundo fibonacci NO es primo\n")    




def punto3():
    print("\n3. se tiene una cantidad de ternas (3 valores numericos por terna)correspondientes a lso lados de triangulos "
            "determinar cuantos triangulos equilateros, escalenos e isosceles se encuentran en estos y si la suma de los "
            "perimetros de los triangulos equilateros es un numero fibonacci")
    ct=int(input("ingrese la cantidad de ternas a digitar : "))
    se=0
    si=0
    ses=0
    sle=0
    for i in range(ct):
        print(f"\nTerna N° {i+1}")
        a=int(input("ingrese el valor a : "))
        b=int(input("ingrese el valor b : "))
        c=int(input("ingrese el valor c : "))
        
        if a>0 and b>0 and c>0:
            if a==b:
                if b==c:
                    print("triangulo equilatero")
                    sle+=a*3
                    se+=1
                else:
                    print("triangulo isoceles")
                    si+=1
            else:
                if a==c:
                    print("triangulo isoceles")
                    si+=1
                else:
                    if b==c:
                        print("triangulo isoceles")
                        si+=1
                    else:
                        print("triangulo escaleno")
                        ses+=1
    a=0
    b=1
    t=0
    print(f"\ntriangulos equialteros : {se}")
    print(f"triangulos isoceles : {si}")
    print(f"triangulos escalenos : {ses}\n")

    while t<sle:
        t=a+b
        a=b
        b=t
    if t == sle:
        return print(f"la suma de los perimetros de los triangulos equilateros : {sle}, es un numero primo\n")
    else:
        return print(f"la suma de los perimetros de los triangulos equilateros : {sle}, NO es un numero primo\n")



 
def punto4():
    print("\n4. se tiene una cantidad de numeros dada encontrar los 3 primeros fibonacci de acuerdo al orden de "
            "entrada y determinar el promedio de los numros pares entre el mayor y el menor de estos fibonacci")
    cd=int(input("ingrese la cantidad de datos "))
    c=0
    for i in range(cd):
        num=int(input("ingrese el numero : "))
        a=0
        b=1
        t=0
        while t<num:
            t=a+b
            a=b
            b=t
        if t==num:
            c+=1
            if c==1:
                f1=num
            elif c==2:
                f2=num
            elif c==3:
                f3=num
    ma=f1
    me=f1
    if f2>ma:
        ma=f2
    elif f2<me:
        me=f2
    if f3>ma:
        ma=f3
    elif f3<me:
        me=f3
    sp=0
    cp=0
    p=0
    mef=me
    while me<ma:
        if me%2==0:
            sp+=me
            cp+=1
        me+=1
    if cp>0:
        p=sp/cp
    return    print(f"el promedio de los numeros pares que estan entre el fibonacci menor {mef}, y el fibonacci mayor {ma}, es {p}\n")


while True:
    print("<======Menu======>\n")
    print("1) Punto 1")
    print("2) Punto 2")
    print("3) Punto 3")
    print("4) Punto 4\n")
    dig=int(input("digite su opción :"))
    if dig==1:
        punto1()
    if dig==2:
        punto2()
    if dig==3:
        punto3()
    if dig==4:
        punto4()
