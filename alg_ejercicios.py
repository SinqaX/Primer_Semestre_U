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





#INTERCAMBIAR DATO MENOR CON DATO EN LA PRIMERA POSICIONM
v=[]
t=int(input("ingrese el numero de datos del vector : "))

for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
print(v)

for i in range(t):
    me=i#asiganamos la posicion i al menor 
    for j in range(i+1,t):#trabajamos con i+1 para no utilizar el valor ordenano
        if v[j]<v[me]:#comparamos el valor de v[j] con el valor que tiene la posicion me 
            me=j #asignamos la posicion j en la variable me
    aux=v[i]#al aux le asignamos el valor de la posicion i
    v[i]=v[me]#el valor minimo v[me] se coloca en la posicion de i
    v[me]=aux#el auxiliar se coloca en la posicion de el valor minimo osea el me
print(v)





#AGREGAR UN DATO EN EL VECTOR EN ORDEN
v=[]
t=int(input("ingrese el numero de datos del vector : "))
c=0

for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
print(v)

dato=int(input("ingrese el dato a insertar : "))
i=0
while i<t and c==0:

    if dato>v[i]:
        i =i+1
    else:
        c=1
        pos=i
j=t-1
v.append(0)
while j >=pos:
    v[j+1]=v[j]
    j=j-1
v[pos]=dato
print(v)





#ELIMINAR DATO EN EL VECTOR Y RECORRER EL VECTOR
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
c=0
for i in range(t):
    val=int(input("ingrese el dato :"))
    v.append(val)
print(v)
dato=int(input("ingrese el dato a eliminar del vector : "))
j=0
while j<=t and c==0:
    if dato==v[j]:
        c=1
        pos=j
    else:
        j+=1
if c==1:
    v.remove(dato)
    print(v)
else:
    print("el dato no se encontro en el en el vector")





#BUSCAR DATO EN EL VECTOR CON BUSQUEDA BINARIA
v=[10,20,30,40,55,75,85,90,100,120,130,140]
t=len(v)
c=0
dato=int(input("ingresar el dato a buscar : "))
limin=0
limsu=t-1
while limin<=limsu and c==0:
    me=int((limin+limsu)/2)
    if dato==v[me]:
        c=1
    else:
        if dato >v[me]:
            limin=me+1
        else:
            if dato<v[me]:
                limsu=me-1
if c==1:
    print("el ",dato," se encuentra en la posicion : ",me)
else:
    print("el dato ",dato," no se encuentra en el vector")





#DATOS DEL PRIMER VECTOR DETERMINAN EL RANGO PARA DATOS DEL SEGUNDO VECTOR
r=[3,5,4]
dato=[4,7,2,9,6,5,7,8,14,2,9,6]
v1=[]
v2=[]
j=0
i=0
for i in r:
    c=0
    limin=j
    limsu=i + j
    for j in range(limin,limsu):
        if c==0:
            me=dato[j]
            ma=dato[j]
            c=1
        else:
            if dato[j]<me:
                me=dato[j]
            else:
                if dato[j]>ma:
                    ma=dato[j]
    v1.insert(i,me)
    v2.insert(i,ma)
    j=limsu
print("los datos menores de cada intervalo del vector con respecto a los datos de el vector rango son : ",v1)
print("los datos mayores de cada intervalo del vector con respecto a los datos de el vector rango son : ",v2)





#DETERMINAR RANGOS CON VECTOR FIBONNACCI PARA VECTOR DATOS Y SACAR PROMEDIO DE CADA INTERVALO
vf=[]
v=[]
tf=int(input("ingrese la cantidad de datos para el vector de los fibonnacci : "))
for f in range(tf):
    fi=int(input("ingrese los fibonnacci:"))
    vf.append(fi)
t=int(input("ingrese la cantidad de datos para el vector de los datos : "))
for i in range(t):
    val=int(input("ingrese el dato :"))
    v.append(val)
j=0
z=1
for fi in vf:
    r=0
    c=0
    limin=j
    limsu=fi+j
    for val in range(limin,limsu):
        r+=+v[val]
        c+=1
    p=r/c
    print("el promedio del rango ",z," sobre el vector de datos es ",p)
    z+=1
    j=limsu





#matriz filas pares impares
matriz=[]
filas=int(input("ingrese la cantidad de filas :"))
columnas=int(input("ingrese la cantidad de columnas :"))
for i in range(filas):
    fila=[]
    for j in range(columnas):
        if i%2==0:
            valor=1
        else:
            valor=0
        fila.append(valor)
    matriz.append(fila)
for fila in matriz:
    print(fila)





#columnas pares impares
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
for i in range(fm):
    fm=[]
    for j in range(cm):
        if j%2==0:
            val=1
        else:
            val=0
        fm.append(val)
    m.append(fm)
for fm in m:
    print(fm)





#diagonal principal secundaria con 1 resto con 0
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
for i in range(fm):
    fila=[]
    for j in range(cm):
        if j==i or j+i==fm-1:
            val=1
        else:
            val=0
        fila.append(val)
    m.append(fila)
for fila in m:
    print(fila)





#promedio pares en matriz
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
s=0
c=0
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    for j in range(cm):
        if fl[j]%2==0:
            s+=fl[j]
            c+=1
if c>0:
    p=s/c  
for fl in m:
    print(fl)
print("el promedio de los numeros pares de la matriz es :",p)





#formar vector con primos iguales en matrices
a=[]
fa=int(input("ingrese la cantidad de filas de la matriz a : "))
ca=int(input("ingrese la cantidad de columnas de la matriz a : "))
b=[]
fb=int(input("ingrese la cantidad de filas de la matriz b : "))
cb=int(input("ingrese la cantidad de columnas de la matriz b : "))
c=[]
l=0
primo=0
for i in range(fa):
    fa=[]
    for j in range(ca):
        val=int(input("ingrese el dato de la  matriz a: "))
        fa.append(val)
    a.append(fa)
for fa in a:
    print(fa)
for x in range(fb):
    fb=[]
    for y in range(cb):
        val=int(input("ingrese el dato de la  matriz b: "))
        fb.append(val)
    b.append(fb)
for fb in b:
    print(fb)
for fa in a:
    s=False
    for i in range(ca):
        r=2
        z=0
        while r<fa[i] and z<=1:
            if fa[i]%2==0:
                z+=1
        if z==1:
            primo=fa[i]
            s=True
            break
for fb in b:
    for x in range(cb):
        if fb[x]%2==0:
            if fb[x]==primo:
                e=0
                k=0
                for k in c:
                    if l==0:
                        c.append(primo)
                        l=1
                    else:
                        if c[k]==primo:
                            e=1
                    if e==0:
                        c.append(primo)
print(c)





#promedio fibonnacci en matriz
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
s=0
c=0
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    for j in range(cm):
        a=0
        b=1
        t=0
        while t<fl[j]:
            t=a+b
            a=b
            b=t
        if t==fl[j]:
            s+=fl[j]
            c+=1
if c>0:
    p=s/c
for fl in m:
    print(fl)
print("el promedio de los fibonnacci es : ",p )





#promedio fibonnacci y pares  en matriz y compararlos
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
s=0
c=0
ss=0
cc=0
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    for j in range(cm):
        a=0
        b=1
        t=0
        while t<fl[j]:
            t=a+b
            a=b
            b=t
        if t==fl[j]:
            s+=fl[j]
            c+=1
        if fl[j]%2==0:
            ss+=fl[j]
            cc+=1
if c>0:
    p=s/c
if cc>0:
    pp=ss/cc
for fl in m:
    print(fl)
if p>pp:
    print("el promedio de los fibonnacci:",p,"es mayor que el promedio de los numeros pares:",pp)
else:
    print("el promedio de los pares :",pp,"es mayor que el promedio de los numeros fibonnacci:",p)





#promedio dato mayoy y menor y promedio de cada fila
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
s=0
c=0
z=True
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    print(fl)
for fl in m:
    p=0
    a=0
    for j in range(cm):
        a+=fl[j]
        if z==True:
            ma=fl[j]
            me=fl[j]
            z=False
        else:
            if fl[j]>ma:
                ma=fl[j]
            else:
                if fl[j]<me:
                    me=fl[j]
    p=a/cm
    print("el promedio de la fila : ",fl," = ",p)
print("el dato mayoy de la matriz es : ",ma," y el dato menor de la matriz es : ",me)





#pprimo mayor y menor de los primos de la matriz
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
s=0
c=0
z=True
x=False
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    print(fl)
for fl in m:
    for j in range(cm):
        r=2
        x=False
        while r<fl[j] and x==False:
            if fl[j]%r==0:
                x=True
            r+=1
        if x==False:
            if z==True:
               ma=fl[j]
               me=fl[j]
               z=False
            else:
               if fl[j]>ma:
                    ma=fl[j]
               else:
                   if fl[j]<me:
                       me=fl[j]

print("el primo mayor es : ",ma," y el primo menor es ",me,)
        




#segundo y tercer primo suma de los dos numero primo
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
s=0
c=0
z=0
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    for j in range(cm):
        a=0
        b=1
        t=0
        while t<fl[j]:
            t=a+b
            a=b
            b=t
        if t==fl[j]:
            z+=1
            if z==2:
                sf=fl[j]
            else:
                if z==4:
                    cf=fl[j]
print("segundo fibonnacci : ",sf)
print("cuarto fibonnaci : ",cf)
rf=sf+cf
r=2
b=False
while r<rf and b==False:
    if rf%r==0:
        b=True
if b==False:
    print("la suma del segundo  y tercer fibonnacci es un numero primo")
else:
    print("la suma del segundo y cuarto fibonnacci no es un numero primo")





#fibonnacci mayor y menor e intercambiarlos
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
z=True
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    print(fl)
for i in range(fm):
    for k in range(cm):
        a=0
        b=1
        t=0
        while t<m[i][k]:
            t=a+b
            a=b
            b=t
        if t==m[i][k]:
            if z==True:
               ma=m[i][k]
               fa=i
               ca=k
               me=m[i][k]
               fe=i
               ce=k
               z=False
            else:
               if m[i][k]>ma:
                    ma=m[i][k]
                    fa=i
                    ca=k
               else:
                   if m[i][k]<me:
                       me=m[i][k]
                       fe=i
                       ce=k
aux=m[fa][ca]
m[fa][ca]=me
m[fe][ce]=aux
print("matriz resultante")
for fl in m :
    print(fl)





#fibonnacci mayor y menor e intercambiar las filas
m=[]
fm=int(input("ingrese la cantidad de filas :"))
cm=int(input("ingrese la cantidad de columnas :"))
z=True
for i in range(fm):
    fl=[]
    for j in range(cm):
        val=int(input("ingrese el dato de la matriz : "))
        fl.append(val)
    m.append(fl)
for fl in m:
    print(fl)
for i in range(fm):
    for k in range(cm):
        a=0
        b=1
        t=0
        while t<m[i][k]:
            t=a+b
            a=b
            b=t
        if t==m[i][k]:
            if z==True:
               ma=m[i][k]
               fa=i
               me=m[i][k]
               fe=i
               z=False
            else:
               if m[i][k]>ma:
                    ma=m[i][k]
                    fa=i
               else:
                   if m[i][k]<me:
                       me=m[i][k]
                       fe=i
                       
aux=m[fa]
m[fa]=m[fe]
m[fe]=aux
print("matriz resultante")
for fl in m :
    print(fl)



#MAYOR MENOR PROMEDIO MATRIZ COIN FUNCIONES
m=[]
fm=int(input("ingrese la cantidad de filas de la matriz"))
cm=int(input("ingrese la cantidad de columnas de la matriz"))
for i in range(fm):
    f=[]
    for j in range(cm):
        val=int(input("ingrese el dato :"))
        f.append(val)
    m.append(f)
for f in m:
    print("el mayor de la fila es ",max(f))
    print("el menor de la fila es ",min(f))
    prom=sum(f)/len(f)
    print("y el promedio de la fila es ",prom)

for f in m :
    print(f)





#MAYOT MENOR Y PROMEDIO DE CADA COLUMNA
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fm=len(matriz)
cm=len(matriz[0])

for c in range(cm):
    ma=matriz[0][c]
    me=matriz[0][c]
    su=0
    z=False
    for f in matriz:
        aux=f[c]
        su+=aux
        if aux>ma:
            ma=aux
        if aux<me:
            me=aux
    prom=su/fm
    print(f"columna {c+1}")
    print(f"mayor : {ma}")
    print(f"menor : {me}")
    print(f"promedio: {prom}\n")




###	Ordenar las filas pares ascendentemente y las filas impares descendentemente
m=[
    [1,3,2],
    [8,7,9],
    [5,4,6],
    [5,1,9]
]
for f in m:    
    print(f)    
fm=len(m)
cm=len(m[0])
for f in range(fm) :
        if f%2==0:
            m[f].sort()
        else:
            m[f].sort(reverse=True)
for f in m :
     print(f)
###	Ordenar las filas pares ascendentemente y las filas impares descendentemente
m=[
    [1,3,2],
    [8,7,9],
    [5,4,6],
    [5,1,9]
]
for f in m:    
    print(f)    
fm=len(m)
cm=len(m[0])
for f in range(fm) :
        if f%2==0:
            for c in range(cm):
                me=c
                for j in range(c+1,cm):
                    if m[f][j]<m[f][me]:
                         me=j
                m[f][c],m[f][me]=m[f][me],m[f][c]
        else:
             for c in range(cm):
                ma=c
                for j in range(c+1,cm):
                    if m[f][j]>m[f][ma]:
                         ma=j
                m[f][c],m[f][ma]=m[f][ma],m[f][c]
for f in m :
     print(f)


###FUNCION FIBBONACI
def fibbonaci(valor):
    a=0
    b=1
    t=0
    while t<valor:
        t=a+b
        a=b
        b=t
    if t==valor:
        return(True)
    else:
        return(False)