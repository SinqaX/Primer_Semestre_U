#PROMEDIO PRIMOS
cn=int(input("ingrese la cantidad de numeros : "))
nv=1
cp=0
sp=0
ce=0
c=1
while nv<=cn:
    num=int(input("ingrese el numero : "))
    ce=0
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1

    if ce==2:
        cp=cp+1
        sp=sp+num
    nv=nv+1
    c=1

if cp>0:
    pp=sp/cp
    print(sp)
    print(cp)
    print("el promedio de numeros pares es : ",pp)
else:
    print("no hay numeros pares en los numeros ingresados")



