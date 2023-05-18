cd=int(input("ingrese la cantidad de numeros : "))
n=1
r=1
c=1
ce=0
lp=1
cp=0
sp=0
l=1
pfp=0
while n<=cd:
    num=int(input("ingrese el numero : "))
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    if t==num:
        if l==1:
            fma=num
        else:
            if num>fma:
                fma=num
        l=l+1
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1
    if ce==2:
        if lp==1:
            pme=num
        else:
            if num<pme:
                pme=num
        lp=lp+1
    c=1
    ce=0
    n=n+1
if fma>pme:
    li=pme
    while li<=fma:
        if li%2==0:
            sp=sp+li
            cp=cp+1
        li=li+1
else:
    li=fma
    while li<=pme:
        if li%2==0:
            sp=sp+li
            cp=cp+1
        li=li+1
pfp=sp/cp
print("fibonnacci mayor : ",fma," primo menor : ",pme," promedio de pares entre estos dos numeros es : ",pfp)



