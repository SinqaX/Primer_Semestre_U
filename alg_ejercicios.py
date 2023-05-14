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
