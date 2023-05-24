cd=int(input("ingrese la cantidad de numeros : "))
nv=1
r=1
sf=0
sp=0
cp=0
cf=0
c=1
ce=0
while nv<=cd:
    num=int(input("ingrese el nummero : "))
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    if t==num:
        while t>0:
            r=r*t
            t=t-1
        sf=sf+r
        cf=cf+1
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1
    if ce==2:
        while num>0:
            r=r*num
            num=num-1
        sp=sp+r
        cp=cp+1
    nv=nv+1
    r=1
    ce=0
    c=1
print(sp,cp,sf,cf)
pp=sp/cp
pf=sf/cf
if pp>pf:
    print("el promedio de la suma de factoriales primos : ",pp," es mayor que la suma de factoriales fibbonnacci : ",pf)
else:
    print("el promedio de la suma de factoriales fibbonacci : ",pf," es mayor que la suma de factoriales primos : ",pp)


