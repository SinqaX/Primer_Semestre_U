def punto4():
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
    return    print(f"el promedio de los numeros pares que estan entre el fibonacci menor {mef}, y el fibonacci mayor {ma}, es {p}")


while True:
    dig=int(input("que punto quiere ejecutar ?"))
    if dig==4:
            punto4()

















       




        














    





    

    





