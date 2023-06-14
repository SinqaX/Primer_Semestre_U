#algoritmo mayor que todos
n1 = int(input("digite n1 : "))
n2 = int(input("digite n2 : "))
n3 = int(input("digite n3 : "))

if n1 > n2:
    if n1 > n2:
       print(n1, "mayor que todos")
    else: 
       print(n3, "mayor que todos")
else:
   if n2 > n3:
       print(n2, "mayor que todos")
   else:
       print(n3, "mayor que todos")





#algoritmo par, impar
a = int(input("ingrese el numero = "))
r = a % 2
if r==0:
    print("este numero es par")
else:
    print("este numero no es par")




#algoritmo multiplo de 5
a = int(input("ingrese el numero = "))
r = a % 5
if r==0:
    print("este numero es multiplo de 5")
else:
    print("este numero no es multiplo de")




#   EL PRIMERO MULTIPLO DEL SEGUNDO
a = int(input("ingrese el primer numero = "))
b = int(input("ingrese el segundo numero = "))
r = b % a
if r==0:
    print(a, "es multiplo de ", b,)
else:
    print(a, "no es multiplo de ", b,)   




#CONTEO_NUMEROS_PARES
a = int(input("ingrese el numero = "))
b = int(input("ingrese el numero = "))
c = int(input("ingrese el numero = "))
d = int(input("ingrese el numero = "))
cp = int
cp=0
if a%2==0:
    cp=cp+1

if b%2==0:
    cp=cp+1

if c%2==0:
    cp=cp+1

if d%2==0:
    cp=cp+1

print("hay ",cp, " numeros pares")




#PROMEDIO_IMPARES
a=int(input("ingrese el numero = "))
b=int(input("ingrese el numero = "))
c=int(input("ingrese el numero = "))
d=int(input("ingrese el numero = "))
si=int
ci=int
pi=int
ci=0
si=0
if a%2==1:
    si=si+a
    ci=ci+1

if b%2==1:
    si=si+b
    ci=ci+1

if c%2==1:
    si=si+c
    ci=ci+1

if d%2==1:
    si=si+d
    ci=ci+1   

if ci==0:
    print("no hay numeros impares")
else:
    pi=si/ci
    print("el promedio de los numeros impares es :", pi)




#PROMEDIO DE NUMEROS PARES
sp=0
cp=0
pp=float
num=int(input("ingrese el numero : "))

while num>0:
    if num % 2 ==0:
        sp=sp+num
        cp=cp+1
    num=int(input("ingrese el numero : "))

if cp>0:
    pp=sp/cp
    print("el promedio de los numeros pares es ", pp)
else:
    print("no hay numeros pares")




#SUMA DE PARES
cp=0
cd=1
while cd<=4:
    num=int(input("ingrese el numero : "))
    if num%2==0:
        cp=cp+1
    cd=cd+1
 
print ("cantidad de pares es :",cp)




#PROMEDIO_DE_MULTIPLOS_DE_5
cne=int(input("ingrese la cantidad de numeros :"))
sm=0
cn=1
cm=0
while cn<=cne:
    num=int(input("ingrese el numero :"))
    if num%5==0:
        sm=sm+num
        cm=cm+1
    cn=cn+1

p=sm/cm
if cm>0:
    p=sm/cm
    print ("el promedio de los multiplos de 5 es ", p)
else:
    print("no hay numeros multiplos de 5")




# MULTIPLO PRIMEO DEL SEGUNDO
n1=int(input("ingrese el primer numero : "))
n2=int(input("ingrese el primer numero : "))
c=n2
while 0<c:
    c=c-n1

if c==0:
    print("el primero es multiplo del segundo")
else:
    print("el primero no es multiplo del segundo")




#CANTIDAD DE PARES X CANTIDAD DE IMPARES
cn=int(input("ingrese la cantidad de numeros : "))
cd=1
cp=0
ci=0
while cd<=cn:
    num=int(input("ingrese el numero : "))
    cd=cd+1
    if num%2==0:
        cp=cp+1
    else:
        ci=ci+1

r=0
c=1
while c<=ci:
    r=r+cp
    c=c+1

print ("la multiplicacion de la cantidad de numeros pares y la cantidad de numeros impares es : ", r)




#SUMA DE PARES , X3 , X5
cd=int(input("ingrese la cantidad de numeros : "))
cn=1
sumc=0
sump=0 
sumt=0

while cn<=cd:
   num=int(input("ingrese el numero : "))
   cn=cn+1  
   if num%2==0:
     sump=sump+num  

   if num%3==0:
     sumt=sumt+num

   if num%5==0:
     sumc=sumc+num

print ("la suma de pares es ", sump, ", la suma de multiplos de 3 es", sumt, "y la suma de multiplos de 5 es", sumc)




#DETERMINAR EL MAYOR Y EL MENOR
nd=int(input("ingrese la cantidad de datos numericos : "))
c=1
while c<=nd:
    num=int(input("ingrese el numero : "))
    if c==1:
        mayor=num
        menor=num
    else:
        if num>mayor:
           mayor=num
        else:
            if num<menor:
                menor=num
    c=c+1
print("el mayor es ", mayor, " y el menor es ", menor)




#SUMA DE PARES, MULTIPLOS DE 3, MULTIPLOS DE 5 Y HALLAR EL MAYOR Y EL MENOR
cd=int(input("ingrese la cantidad de numeros : "))
cn=1
sumc=0
sump=0 
sumt=0

while cn<=cd:
   num=int(input("ingrese el numero : "))
   if cn==1:
        mayor=num
        menor=num
   else:
        if num>mayor:
           mayor=num
        else:
            if num<menor:
                menor=num
   cn=cn+1 
   if num%2==0:
     sump=sump+num  

   if num%3==0:
     sumt=sumt+num

   if num%5==0:
     sumc=sumc+num

   
print ("la suma de pares es ", sump, ", la suma de multiplos de 3 es", sumt, 
       "y la suma de multiplos de 5 es", sumc, ", el mayor es ", mayor, " y el menor es ", menor)






v=int(input("ingrese la cantidad a retirar, este valor debe estar entre 5000 y 500000 y debe ser multiplo de 5 : "))
cb=0
bc=0
bcc=0
bv=0
bd=0
bcp=0
if 5000<=v<=500000:
    if v%5000==0:
        while v>=100000:
            cb=cb+1
            bc=bc+1
            v=v-100000
        while v>=50000:
            cb=cb+1
            bcc=bcc+1
            v=v-50000
        while v>=20000:
            cb=cb+1
            bv=bv+1
            v=v-20000
        while v>=10000:
            cb=cb+1
            bd=bd+1
            v=v-10000
        while v>=5000:
            cb=cb+1
            bcp=bcp+1
            v=v-5000
        print("se entregan : ", cb, "billetes los cuales : ")
        print( bc, " billete(s) de 100000 ")
        print(bcc, " billete(s) de 50000 ")
        print(bv, " billete(s) de 20000")
        print(bd," billete(s) de 10000 ")
        print(bcp, " billete(s) de 5000")
           
    else:
        print("la cantidad a retirar no es muliplo de 5000")
else:
    print("la cantidad ingresada no esta en el rango")
     





#NUMERO PRIMO
nd=int(input("ingrese el numero : "))
c=1
p=0
while c<=nd:
    if nd%c==0:
        p=p+1
    
    c=c+1

print("la cantidad de divisores exactos es ", p)
if p==2:
    print("el numero ingresado es primo")
else:
    print("el numero ingresado no es primo ")




#TABLAS DEL 1 AL 10
c=1
ac=1
while ac<=10:
 while c<11:
        r=ac*c
        print(ac," x ", c,"=", r)
        c=c+1   
 ac=ac+1
 c=1




 #tablas entre n1 y n2
n1=int(input("ingrese el N1 : "))
n2=int(input("ingrese el N2 : "))
c=1
if n1<n2:
    ct=n1
    while ct<=n2:
        while c<11:
            r=ct*c
            print(ct," x ",c," = ", r)
            c=c+1
        ct=ct+1
        c=1
else:
    ct=n2
    while ct<=n1:
        while c<11:
            r=ct*c
            print(ct," x ",c," = ", r)
            c=c+1
        ct=ct+1
        c=1




#ALGORITMO EXAMEN
cd = int(input("Ingrese la cantidad de números: "))
c = 1
cp = 0
cn = 1
ce = 0
ctm = 0
xt = 0
ct = 0

while cn <= cd:
    num = int(input("Ingrese el número: "))
    c = 1
    ce = 0
    
    while c <= num:
        if num % c == 0:
            ce = ce + 1
        c = c + 1

    if ce == 2:
        cp = cp + 1
    
    if num % 3 == 0:
        ct = ct + 1
     
    cn = cn + 1

print("La cantidad de números primos es", cp, "y la cantidad de múltiplos de 3 es", ct, "y las tablas de multiplicar de números pares entre estos dos números son:")
if cp < ct:
    ctm == cp
    
    while ctm <= ct:
        if ctm % 2 == 0:
            print("TABLA DEL : ",ctm)
            while xt < 11:
              r = ctm * xt
              print(ctm, "x", xt, "=", r)
              xt = xt + 1
        ctm = ctm +1
        xt = 1
        
else:
    ctm == ct
    
    while ctm <= cp:
        if ctm % 2 == 0:
            print("TABLA DEL : ",ctm)
            while xt < 11:
              r = ctm * xt
              print(ctm, "x", xt, "=", r)
              xt = xt + 1
        ctm = ctm +1
        xt = 1




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



#CUMPLE PARA 3 VALORES
cn=int(input("ingrese la cantidad de numeros : "))
nv=1
sf=0
while nv<=cn:
    cf=1
    if cf<=2:
        sf=sf+num
    cf+=cf+1
    nv=nv+1
numf=int(input("ingrese el numero : "))
if sf==numf:
    print("cumple con la sucesion fibonnacci")
else:
    print("no cumple con la sucesion fibonnacci")





#CON LOS ULTIMOS 3 NUMEROS
cn=int(input("ingrese la cantidad de numeros : "))
nv=1
sf=0
while nv<=cn-3:
    num=int(input("ingrese el numero : "))
    nv=nv+1
nums1=int(input("ingrese el numero : ") )
nums2=int(input("ingrese el numero : ") )
numsf=int(input("ingrese el numero : ") )
s=nums1+nums2
if s==numsf:
    print("los ultimos tres numeros son consecutivos ya que la suma de el antepenultimo y penultimo da como resultado el ultimo numero ")
else:
    print("los ultimos tres numeros no son consecutivos")





#MAYOR Y MENOR PRIMOS Y SUMA DE PARES ENTRE ESOS
nd=int(input("ingrese la cantidad de numeros : "))
sp=0
cd=1
cp=1
ce=0
c=1
lp=1
while cd<=nd:
    num=int(input("ingrese el numero : "))
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1
    if ce==2:
        if lp==1:
            pma=num
            pme=num
        else:
            if num>pma:
                pma=num
            else:
                if num<pme:
                    pme=num
        lp=lp+1
    ce=0
    c=1
    cd=cd+1
cpm=pma
np=pme
while np<=cpm:
    if np%2==0:
        sp=sp+np
    np=np+1
print("n primo mayor : ",pma," n primo menor : ",pme, " suma de pares entre esos primos : ",sp)





#PRIMO MAYOR MENOR Y RESTA 
nd=int(input("ingrese la cantidad de numeros : "))
sp=0
cd=1
cp=1
ce=0
c=1
lp=1
while cd<=nd:
    num=int(input("ingrese el numero : "))
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1
    if ce==2:
        if lp==1:
            pma=num
            pme=num
        else:
            if num>pma:
                pma=num
            else:
                if num<pme:
                    pme=num
        lp=lp+1
    ce=0
    c=1
    cd=cd+1
print("primo mayo",pma,"primo menor",pme)
cr=1
cer=0
r=pma-pme
while cr<=r:
    if r%cr==0:
        cer=cer+1
    cr=cr+1
if cer==2:
    print("la resta de los numeros primos mayor y menor da como resultado un numero primo")
else:
    print("la resta de los numeros primos mayor y menor no da como resultado un numero primo")





#TIPO EXAMEN SEGUNDO Y TERCER PRIMO MULTIPLICADO CON SUMAS
nd=int(input("ingrese la cantidad de numeros : "))
cn=1
cp=0
c=1
ce=0
r=0
while cn<=nd:
    num=int(input("ingrese el numero : "))
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1
    if ce==2:
        cp=cp+1

        if cp==2:
         sp=num
        else:
         if cp==3:
          tp=num
    cn=cn+1
    c=1
    ce=0
cl=1
while cl<=tp:
    r=r+sp
    cl=cl+1
print("el segundo primo es",sp,"y el tercer primo es ",tp," y la multiplicacion de esos dos es",r)




#TIPO EXAMEN PRIMOS MAYOR, MENOR SUMA FACTORIALES PRIMOS
cd=int(input("ingrese la cantidad de datos : "))
nv=1
cw=1
ce=0
lp=1
r=1
sp=0
while nv<=cd:
    num=int(input("ingrese el numero : "))
    while cw<=num:
        if num%cw==0:
            ce=ce+1
        cw=cw+1
    if ce==2:
        if lp==1:
            pma=num
            pme=num
        else:
            if num>pma:
                pma=num
            else:
                if num<pme:
                    pme=num
        lp=lp+1
    cw=1
    ce=0
    nv=nv+1
clm=pma
li=pme
while li<=clm:
    if li%2==0:
        pp=li
        while pp>0:
            r=r*pp
            pp=pp-1
        sp=sp+r
    li=li+1
    r=1
print("primo mayor : ",pma," primo menor : ",pme," y la suma de factoriales pares entre estos numeros es : ",sp)





#SERIE FIBONNACCI
cf=int(input("ingrese la cantidad final : "))
a=0
b=1
t=0
print(a)
print(b)
while t<=cf:
    t=a+b
    if t<=cf:
     print(t)
     a=b
     b=t

    
    
    
    
    #SERIE FIBONNACCI HASTA LOS QUE QUIERE
cf=int(input("ingrese la cantidad de fibonnacci que quiere : "))
a=0
b=1
t=0
cp=3
print("1 =",a)
print("2 =",b)
while cp<=cf:
    t=a+b
    print( cp," =",t)
    a=b
    b=t
    cp=cp+1
    
    
    
    
    
    #CALCULAR SI UN NUMERO ES FIBONNACCI
c=int(input("ingrese el numero : "))
a=0
b=1
t=0

while t<c:
    t=a+b
    a=b
    b=t
if t==c:
    print("si es fibonnacci")    
else:
    print("no es fibonnacci")
    
    
    
    
    
    #PROMEDIO FIBONNACCI
c=int(input("ingrese la cantidad dada de numeros : "))
cn=1
sf=0
cf=0
while cn<=c:
    num=int(input("ingrese el numero"))
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    if t==num:
        sf=sf+num
        cf=cf+1
    cn=cn+1
    
pf=sf/cf
print(sf)
print(cf)
print("promedio d enumeros fibonnacci : ",pf)





#FIBONNACCI MAYOR Y MENOR
c=int(input("ingrese la cantidad de numeros : "))
nv=1
lf=1

while nv<=c:
    num=int(input("ingrese el numero : "))
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    if t==num:
        if lf==1:
            fma=num
            fme=num
        else:
            if num>fma:
                fma=num
            else:
                if num<fme:
                    fme=num
        lf=lf+1
    nv=nv+1
print("fibonnacci mayor : ", fma ," fibonnacci menor : ",fme)
     




#FIBONNACCI MAYOR PRIMO MENOR PROMEDIO PARES
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

#2 Y 3 FIBONNACCI SUMA PRIMO
cd=int(input("ingrese la cantidad de numeros a digitar : "))
nv=1
cf=0
sf=0
c=1
ce=0
while nv<=cd:
    num=int(input("ingrese el numero : "))
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    if t==num:
        cf=cf+1
        if cf==2:
         sf=sf+num
         print(sf)
        if cf==3:
         sf=sf+num
         print(sf)
    nv=nv+1
while c<=sf:
    if sf%c==0:
        ce=ce+1
    c=c+1
if ce==2:
    print("la suma del segundo y tercer fibonnacci es un numero primo")
else:
    print("la suma del segundo y tercer fibonnacci no es un numero primo")
    




#EXAMEN ANDHANCK
cd=int(input("ingrese el la cantidad de datos : "))
nv=1
sf=0
while nv<=cd:
    num=int(input("ingrese el numero : "))
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    nv=nv+1
if t==num:
        print("son consecutivos")
else:
    print("no son consecutivos")





    #EJEMPLO EXAMEN MIO
cd=int(input("ingrese la cantidad de datos : "))
nv=1
c=1
ce=0
cp=0
ct=0
r=0
while nv<=cd:
    num=int(input("ingrese el numero : "))
    while c<=num:
        if num%c==0:
            ce=ce+1
        c=c+1
    if ce==2:
        cp=cp+1
    if num%3==0:
        ct=ct+1
    c=1
    ce=0
    nv=nv+1
print("la cantidad de primos es : ",cp," y la cantidad de multiplos de 3 es : ",ct," y los numeros fibonnacci que se encuentran entre estos dos contadores es :")
if cp<ct:
    while cp<ct:
        a=0
        b=1
        t=0
        while t<cp:
            t=a+b
            a=b
            b=t
        if t==cp:
            ls=1
            print("TABLA DEL ",cp)
            while ls<11:
                r=cp*ls
                print(cp," * ",ls," = ",r)
                ls=ls+1
        cp=cp+1
        r=0
else:
    while ct<cp:
        a=0
        b=1
        t=0
        while t<ct:
            t=a+b
            a=b
            b=t
        if t==ct:
            ls=1
            print("TABLA DEL ",cp)
            while ls<11:
                r=ct*ls
                print(ct," * ",ls," = ",r)
                ls=ls+1
        ct=ct+1
        r=0





#EJERCICIO SEGUNDO Y CUARTO PRIMO CONSECUTIVO
cd=int(input("ingrese la cantidad de numeros : "))
nv=1
b=0
c=2
cp=0
l=0
zp=0
sp=0
ap=0
while nv<=cd:
    num=int(input("ingrese el numero : "))
    while c<num and b==0:
        if num%c==0:
            b=0
        else:
            b=1
        c=c+1
    if b==0:
        cp=cp+1
    if cp==2:
        sp=num
    else:
        if cp==4:
            ap=num
    nv=nv+1
    c=2
if sp<ap:
    spd=sp+1
    while spd<=ap:
        while cp<ap and l==0:
            if spd%c==0:
                l=0
            else:
                l=1
        if l==0:
            zp=zp+1
        spd=spd+1
    if zp==0:
        print("el segundo y cuarto primo son consecutivos")
    else:
        print("no lo son")
else:
    apd=ap+1
    while apd<=sp:
        while cp<sp and l==0:
            if apd%c==0:
                l=0
            else:
                l=1
        if l==0:
            zp=zp+1
        apd=apd+1
    if zp==0:
        print("el segundo y cuarto primo son consecutivos")
    else:
        print("no lo son")





#SUMA FACTORIALES FIBONNACCI
cd=int(input("ingrese la cantidad de numeros a sumas : "))
nv=1
r=1
sf=0
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
    r=1
    nv=nv+1

print(sf)





#COMPARAR SUMA FAC PRIMOS Y FIBONNACCI
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
    


#PROMEDIO PRIMOS VECTOR    
v =[]
s=0
cc=0
t=int(input("ingrese la cantidad de datos del vector : "))
for i in range(t):
    val=int(input("ingrese el valor : "))
    v.append(val)
for i in range(t):
    r=2
    c=0
    while r<v[i]-1 and c==0:
        if v[i]%2==0:
            c=1
        r=r+1
    if c==0:
        s=s+v[i]
        cc=cc+1
if cc>0:
    p=s/cc
    print("promedio primos : ",p)
else:
    print("no hay primos en el vector")
    
    
    

#PROMEDIO FIBONNACCI VECTOR
v =[]
s=0
c=0
t=int(input("ingrese la cantidad de datos del vector : "))
for i in range(t):
    val=int(input("ingrese el valor : "))
    v.append(val)
for i in range(t):
    a=0
    b=1
    t=0
    while t<v[i]:
        t=a+b
        a=b
        b=t
    if t==v[i]:
        s=s+v[i]
        c=c+1
if c>0:
    p=s/c
    print("promedio fibonnacci : ",p)
else:
    print("no hay fibonnacci en el vector")






#ROMPIMIENTO DE CONTROL
cc=int(input("ingrese el valor : "))
while cc>0:
    cau=cc
    g=0
    while cau==cc:
        g=g+1
        cc=cc=int(input("ingrese el valor : "))
    print("grupo del ",cau," : cantidad = ",g)





#DECISION DEL USUARIO
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





#MAYOR MENOR DE UN VECTOR
t=int(input("ingrese la cantidad de datos del vector : "))
v=[]
men=0
may=0
for i in range(t):
    val=int(input("ingrese el dato"))
    v.append(val)
for i in range(t):
    if i==1:
        may=v[i]
        men=v[i]
    else:
        if v[i]>may:
            may=v[i]
        else:
            if v[i]<men:
                men=v[i]
print("dato mayor : ",may)
print("dato menor : ",men)




#FIBONNACCI MENOR VECTOR
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
cp=0
men=0
c=0
for i in range(t):
    val=int(input("ingrese el valor : "))
    v.append(val)
for i in range(t):
    a=0
    b=1
    t=0
    while t<v[i]:
        t=a+b
        a=b
        b=t
    if t==v[i]:
        if cp==0:
            men=v[i]
            cp=1
        else:
            if v[i]<men:
                men=v[i]
print("fibonnacci menor : ",men)





# MENOR VECTOR
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
cp=0
men=0
for val in range(t):
    val=int(input("ingrese el valor : "))
    v.append(val)
for val in range(t):
    if cp==0:
        men=v[val]
        cp=1
    else:
        if v[val]<men:
            men=v[val]
v.remove(men)
v.insert(0, men)

print (v)





#VALOR A ENCONTRAR EN EL VECTOR
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
c=0
s=0
for i in range(t):
    val=int(input("ingrese el valor : "))
    v.append(val)
k=int(input("ingrese el dato a encoontrar : "))
for i in range(t):
    if k==v[i]:
        print("el dato ",k," se encuentra en la posición ", i)
        s=1
if s==0:
    print("el dato a buscar no se eencuentra en el vector")            





#PRIMEROS DOS PRIMOS CONSECUTIVOS
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
cp=1
pp=0
sp=0
z=0
for i in range(t):
    val=int(input("ingrese el dato : "))
    v.append(val)
for i in range(t):
    r=2
    c=0
    while r<v[i]-1 and c==0:
        if v[i] % r == 0:
            c=1
        r=r+1
    if c==0 and cp<=2:
        if cp==1:
            pp=v[i]
            cp=2
        else:
            if cp==2:
                sp=v[i]
                cp=3
if pp<sp:
    pp=pp+1
    for pp in range(sp-1) :
        r=2
        c=0
        while r<pp and c==0:
            if pp%r==0:
                c=c+1
            r=r+1
        if c==0:
            z=z+1
    if z==0:
        print("los primeros dos primos son consecutivos")
    else:
        print("no son consecutivos los primeros dos primos")
else:
    sp=sp+1
    for sp in range(pp-1) :
        r=2
        c=0
        while r<sp and c==0:
            if sp%r==0:
                c=c+1
            r=r+1
        if c==0:
            z=z+1
    if z==0:
        print("los primeros dos primos son consecutivos")
    else:
        print("no son consecutivos los primeros dos primos")





#REMPLAZAR VECTOR CON LA MULTIPLICAICON DEL MAYOR Y EL MENOR
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
c=0
me=0
ma=0
r=1
rr=0
for i in range(t):
    val=int(input("ingrese el valor : "))
    v.append(val)
for i in range(t):
    if c==0:
        ma=v[i]
        me=v[i]
        c=1
    else:
        if v[i]>ma:
            ma=v[i]
        else:
            if v[i]<me:
                me=v[i]
while r<=me:
    rr=rr+ma
    r=r+1
p1=v.index(me)
p2=v.index(ma)
for i in range(t):
    if i>p1 and i<p2:
        v[i]=rr
print(v)





#FIBONACCI MAYOR MENOR REMPLAZAR CON EL MENOR TOD EL VECTOR
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
c=0
for i in range(t):
    val=int(input("ingrese el dato : "))
    v.append(val)
for i in range(t):
    a=0
    b=1
    ta=0
    while ta<v[i]:
        ta=a+b
        a=b
        b=ta
    if ta==v[i]:
        if c==0:
            ma=v[i]
            me=v[i]
            c=1
        else:
            if v[i]>ma:
                ma=v[i]
            else:
                if v[i]<me:
                    me=v[i]
#con este ciclo quiero remplazar todos los valores de el vector por el valor de la variable me
for i in range(t):
   v[i]=me
print("fibonnacci menor : ",me," fibonnacci mayor : ",ma)
print(v)





#ORDEN LISTA MENOR A MAYOR
v=[]
t=int(input("ingrese el numero de datos del vector : "))
c=0
me=0
s=0
for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
print (v)
for i in range(t):
    if c==0:
        me=v[i]
        c=1
    else:
        if me>v[i]:
            me=v[i]
            v.pop(i)
            v.insert(0, me)
print(v)





#ORDEN LISTA MENOR A MAYOR
v=[]
t=int(input("ingrese el numero de datos del vector : "))
c=0
me=0
s=0
for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
print (v)
v.sort()
print(v)





#CUANTAS VECES SE REPITE UN NUMERO EN EL VECTOR
v=[]
t=int(input("ingrese el numero de datos del vector : "))
c=0
for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
s=int(input("ingrese el numero que quiere buscar cauntas veces se repite en el vector : "))
for i in range(t):
    if s==v[i]:
        c=c+1
if c>0:
    print("el numero ",s," se repite ",c," veces en el vector")
else:
    print("el numero ingresado no se encuentra en el vector")





#CUANTAS VECES SE REPITE LOS DATOS  EN EL VECTOR
v=[]
t=int(input("ingrese el numero de datos del vector : "))
for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
for i in range(t):
    c=v[i]
    co=0
    for i in range(t):
        if c==v[i]:
            co=co+1
        print("el numero ",c," se repite ",co," veces")





#CUANTAS VECES SE REPITE LOS DATOS  EN EL VECTOR
v=[]
t=int(input("ingrese el numero de datos del vector : "))
for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
for z in set(v):
    c=v.count(z)
    print("el numero ",z," se repite ",c," veces")





#VECTOR CON NUMEROS SIN REPETIR
v=[]
v2=[]
t=int(input("ingrese la cantidad de datos del vector : "))
for val in range(t):
    val=int(input("ingrese el dato"))
    v.append(val)
v2=[set(v)]
print(v)
print(v2)





#VECTOR CON NUMEROS SIN REPETIR
v=[]
v2=[]
t=int(input("ingrese la cantidad de datos del vector : "))
for val in range(t):
    val=int(input("ingrese el dato"))
    v.append(val)
for val in v:
    if val not in v2:
        v2.append(val)
print(v)
print(v2)





#NUMERO DE VECES QUE SE REPITE CADA NUMERO EN EL VECTOR
v=[]
c=[]
t=int(input("ingrese la cantidad de datos del vector : "))
for val in range(t):
    val=int(input("ingrese el dato"))
    v.append(val)
for val in v:
    z=v[val]
    co=0
    for i in range(t):
        if z==v[i]:
           co=co+1
    if val not in c:
        c.append(val)
        print("el ",val," se repite ",co," veces")





#NUMERO DE VECES QUE SE REPITE CADA NUMERO EN EL VECTOR Y EL QUE MAS SE REPITE
v=[]
c=[]
t=int(input("ingrese la cantidad de datos del vector : "))
a=0
ma=0
zi=0
for val in range(t):
    val=int(input("ingrese el dato"))
    v.append(val)
for val in v:
    z=v[val]
    co=0
    for i in range(t):
        if z==v[i]:
           co=co+1
    if a==0:
        ma=co
        a=1
    else:
        if co>ma:
            ma=co
            zi=v[val]
    if val not in c:
        c.append(val)
        print("el ",val," se repite ",co," veces")
print("el dato que mas se repite es el ",zi," con ",ma," veces")