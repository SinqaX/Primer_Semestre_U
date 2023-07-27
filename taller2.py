#Se tiene varios datos numéricos positivos donde el ultimo dato es un negativo, realizar los siguiente:

#	Determinar el primo mayor y el primo menor
n=0
pma=0
pme=0
num=int(input("ingrese el dato numerico : "))
while num>0:
    p=False
    r=2
    while r<num and p==False:
        if num % r==0:
            p=True
        r+=1
    if p==False:
        if n==0:
            pma=num
            pme=num
            n=1
        else:
            if num>pma:
                pma=num
            else:
                if num<pme:
                    pme=num
    num=int(input("ingrese el dato numerico : "))
print("el primo mayor es : ",pma," y el primo menor es : ",pme)
    
#	Determinar el promedio de los números primos
pma=0
pme=0
sum=0
c=0
num=int(input("ingrese el dato numerico a : "))
while num>0:
    p=False
    r=2
    while r<num and p==False:
        if num % r==0:
            p=True
        r+=1
    if p==False:
        sum+=num
        c+=1
    num=int(input("ingrese el dato numerico : "))
if c>0:
    p=sum/c
    print("el promedio de los numeros primos es : ",p)
else:
    print("no hay numeros primos en los datos ingresados")

#	Determinar el factorial del primo mayor y el factorial del Fibonacci menor
f=0
c=0
num=int(input("ingrese el dato numerico : "))
while num>0:
    a=0
    b=1
    t=0
    while t<num:
        t=a+b
        a=b
        b=t
    if t==num:
        if f==0:
            fm=num
            f=1
        else:
            if num<fm:
                fm=num
    r=2
    p=False
    while r<num and p==False:
        if num%r==0:
            p=True
        r+=1
    if p==False:
        if c==0:
            pm=num
            c=1
        else:
            if num>pm:
                pm=num
    num=int(input("ingrese el dato numerico : "))
    
print("primo mayor : ",pm)
print("fibonnacci menor : ",fm )
z=1
while pm>0:
    z*=pm
    pm-=1
x=1
while fm>0:
    x*=fm
    fm-=1

print("el factorial del primo mayor es : ",z," y el factorial del fibonnacci menor es : ",x)



#Se tienen varias ternas de datos, correspondientes a los lados de triángulos 
#cuya entrada está controlada por el usuario, realizar lo siguiente:

#	Determinar si la cantidad de triángulos isósceles es un número primo
equilatero=0
isoceles=0
escaleno=0
resp=input("desea procesar triangulos ? (s/n) : ")
while resp=='s'or resp=='S':
    a=int(input("ingrese el valor a : "))
    b=int(input("ingrese el valor b : "))
    c=int(input("ingrese el valor c : "))
    if a>0 and b>0 and c>0:
        if a==b:
            if b==c:
                 equilatero+=1
            else:
                 isoceles+=1
        else:
            if a==c:
                isoceles+=1
            else:
                if b==c:
                    isoceles+=1

    resp=input("desea procesar triangulos ? (s/n) : ")
r=2
p=False
while r<isoceles and p==False:
    if isoceles%r==0:
        p=True
    r+=1
if p==False:
    print("la cantidad de triangulos isoceles SI es un numero primo")
else:
    print("la cantidad de triangulos isoceles NO es un numero primo")

#	Comparar el promedio de los perímetros de los equiláteros con el promedio de los escalenos
equilatero=0
isoceles=0
escaleno=0
sume=0
sumi=0
sumes=0
resp=input("desea procesar triangulos ? (s/n) : ")
while resp=='s'or resp=='S':
    a=int(input("ingrese el valor a : "))
    b=int(input("ingrese el valor b : "))
    c=int(input("ingrese el valor c : "))
    if a>0 and b>0 and c>0:
        if a==b:
            if b==c:
                sume+=a+b+c
                equilatero+=1
        else:
            if a==c:
                sumi+=a+b+c
                isoceles+=1
            else:
                if b==c:
                    sumi+=a+b+c
                    isoceles+=1
                else:
                    sumes+=a+b+c
                    escaleno+=1
    resp=input("desea procesar triangulos ? (s/n) : ")
if equilatero>0:
    prom_equil=sume/equilatero
if escaleno>0:
    prom_escal=sumes/escaleno
if prom_equil==prom_escal:
    print("el promedio de los perimetros de los triangulos equilateros ES IGUAL con respecto al promedio de los perimetros de los triangulos escalenos")
else:
    if prom_equil>prom_escal:
        print("el promedio de los perimetros de los triangulos equilateros ES MAYOR con respecto al promedio de los perimetros de los triangulos escalenos")
    else:
        print("el promedio de los perimetros de los triangulos equilateros ES MENOR con respecto al promedio de los perimetros de los triangulos escalenos")

#	Determinar el factorial del contador de triángulos equiláteros
equilatero=0
isoceles=0
escaleno=0
f=1
resp=input("desea procesar triangulos ? (s/n) : ")
while resp=='s'or resp=='S':
    a=int(input("ingrese el valor a : "))
    b=int(input("ingrese el valor b : "))
    c=int(input("ingrese el valor c : "))
    if a>0 and b>0 and c>0:
        if a==b:
            if b==c:
                 equilatero+=1
    resp=input("desea procesar triangulos ? (s/n) : ")
if equilatero>0:
    while equilatero>0:
        f*=equilatero
        equilatero-=1
    print("el factorial de la cantidad de triangulos equilateros es : ",f)
else:
    print("no hay triangulos equilateros ingresados")



#Se tiene varios datos numéricos repetidos y agrupados  donde el último dato es un -5, realizar los siguiente:

#	Determinar los contadores de cada grupo y mostrar la suma de aquellos contadores que son números pares
sum_pares=0
cc=int(input("ingrese el valor : "))
while cc!=-5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    if g%2==0:
        sum_pares+=g
print("la suma de los contadores pares es : ",sum_pares)

#	Determinar si la suma de los contadores de cada grupo es un numero Fibonacci
sum=0
cc=int(input("ingrese el valor : "))
while cc!=-5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    sum+=g
a=0
b=1
t=0
while t<sum:
    t=a+b
    a=b
    b=t
if t==sum:
    print("la suma de los contadores SI es un numero fibonacci")
else:
    print("la suma de los contadores NO es un numero fibonacci")

#-	Determinar los contadores de cada grupo y mostrar el promedio de aquellos contadores que son números Fibonacci.
sum=0
c=0
cc=int(input("ingrese el valor : "))
while cc!=-5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    a=0
    b=1
    t=0
    while t<g:
        t=a+b
        a=b
        b=t
    if t==g:
        sum+=g
        c+=1
if c>0:
    prom=sum/c
    print("el promedio de los contadores que son numeros fibonacci es : ",prom)
else:
    print("no hay contadores que sean numeros fibonnacci")

#-	Determinar los contadores de cada grupo y mostrar el promedio de aquellos contadores que son números primos
sum=0
c=0
cc=int(input("ingrese el valor : "))
while cc!=-5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    r=2
    p=False
    while r<g and p==False:
        if g%r==0:
            p=True
        r+=1
    if p==False:
        sum+=g
        c+=1
if c>0:
    prom=sum/c
    print("el promedio de los contadores que son numeros primos es : ",prom)
else:
    print("no hay contadores que sean numeros primos")

#-	Determinar cual es el grupo que más se repite
c=0
grupo_ma=[]
cc=int(input("ingrese el valor : "))
while cc!=-5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    if c==0:
        rep_may=g
        c=1
        grupo_ma.append(caux)
    else:
        if g>rep_may:
            rep_may=g
            grupo_ma.append(caux)
        elif g==rep_may:
            grupo_ma.append(caux)

print("el(los) grupo(s) que mas se repite(n) es(son) el(los) del ",grupo_ma," con ",rep_may," repeticiones")

#-	Determinar si el grupo que menos se repite es un número primo
c=0
aux=0
cc=int(input("ingrese el valor : "))
while cc != -5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    if c==0:
        rep_men=g
        c=1
        aux=caux
    else:
        if g<rep_men:
            rep_may=g
            aux=caux
r=2
p=False
while r<aux and p==False:
    if aux%r==0:
        p=True
    r+=1
if p==False:
    print("el grupo que menos se repite es el del",aux," el cual es un numero primo")
else:
    print("el grupo que menos se repite es el del",aux," el cual NO ES un numero primo")

#-	Determinar cual es el promedio de datos por grupo
sum=0
c=0
cc=int(input("ingrese el valor : "))
while cc!=-5:
    caux=cc
    g=0
    while caux==cc:
        g+=1
        cc=int(input("ingrese el valor : "))
    sum+=g
    c+=1
prom=sum/c
print("el promedio de datos por grupo es : ",prom)



#Ejercicios con vectores

#1.	Se tiene un vector con datos numéricos repetidos, determinar cuál es el primo que más se repite.
v=[]
t=int(input("ingrese la cantidad de datos que va a tener el vector : "))
for i in range(t):
    val=int(input("ingresar dato : "))
    v.append(val)
rep=0
for i in range(t):
    r=2
    p=False
    while r<v[i]-1 and p==False:
        if v[i]%r==0:
            p=True
        r+=1
    if p==False:
        aux=v[i]
        c=0
        for i in range(t):
            if aux==v[i]:
                c+=1
    if i==0:
        rep=c
        primo=aux
    else:
        if c>rep:
            rep=c
            primo=aux
print("el primo que mas re repite es el : ",primo," con ",rep, " repeticiones")

#2.	Se tiene un vector con datos numéricos eliminar los números pares.
v=[]
t=int(input("ingrese la cantidad de datos que va a tener el vector : "))
for i in range(t):
    val=int(input("ingresar dato : "))
    v.append(val)
print("vector ingresado : ",v)
i=0
while i<len(v):
    if v[i]%2==0:
        v.pop(i)
    else:
        i+=1
print("vector resultante : ",v)

#3.	Se tiene un vector con datos numéricos eliminar los datos que sean primos y Fibonacci.
v=[]
t=int(input("ingrese la cantidad de datos que va a tener el vector : "))
for i in range(t):
    val=int(input("ingresar dato : "))
    v.append(val)
print("vector ingresado : ",v)
i=0
while i<len(v):
    r=2
    p=False
    while r<v[i] and p==False:
        if v[i]%r==0:
            p=True
        r+=1
    if p==False:
        v.pop(i)
    else:
        a=0
        b=1
        z=0
        while z<v[i]:
            z=a+b
            a=b
            b=z
        if z==v[i]:
            v.pop(i)
        else:
            i+=1
print("vector resultante : ",v)

#4.	Se tiene un vector ordenado con datos numéricos, insertar varios datos en la posición que le corresponde
v=[]
t=int(input("ingrese el numero de datos del vector : "))
for i in range(t):
    val=int(input("ingresse el dato : "))
    v.append(val)
print("vector ingresado : ",v)
ndi=int(input("ingrese el numero de datos a insertar : "))
for z in range(ndi):
    dato = int(input("Ingrese el dato a insertar: "))
    i = 0
    while i < len(v) and dato > v[i]:
        i += 1
    v.insert(i, dato)
print("vector resultante : ",v)

#5.	Leer una serie de datos numéricos y llenarlos en un vector de tal forma que vayan quedando ordenados ascendentemente
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
for i in range(t):
    val=int(input("ingrese el dato : "))
    if i==0:
        v.append(val)
    else:
        i=0
        while i<len(v) and val>v[i]:
            i+=1
        v.insert(i, val)
    print("vector resultante ",v)

#6.	Leer una serie de datos numéricos y llenarlos en un vector 
#los datos que sean primos y Fibonacci que vayan quedando ordenados descendentemente.
v=[]
t=int(input("ingrese la cantidad de datos del vector : "))
for i in range(t):
    val=int(input("ingrese el dato : "))
    if i==0:
        v.append(val)
    else:
        for i in range(t):
            r=2
            p=False
            while r<v[i] and p==False:
                if v[i]%r==0:
                    p=True
                r+=1
            if p==False:
                i=0
                while i<t and val<v[i]:
                    i+=1
                v.insert(i,val)
            else:
                a=0
                b=1
                z=0
                while z<v[i]:
                    z=a+b
                    a=b
                    b=z
                if z==v[i]:
                    j=0
                    while j<t and val<v[i]:
                        j+=1
                    v.insert(j,val)
            break
    print("vector resultante ",v)

#7.	Se tiene un vector con datos numéricos, ordenar las 
# posiciones pares en orden ascendente y las impares en orden descendente.
v = [6, 10, 2, 8, 7, 3, 11, 17]
t = len(v)
pa = []
im = []

for i in range(t):
    if i % 2 == 0:
        pa.append(v[i])
    else:
        im.append(v[i])
for i in range(len(pa)):
    me = i
    for j in range(i + 1, len(pa)):
        if pa[j] < pa[me]:
            me = j
    pa[i], pa[me] = pa[me], pa[i]

for i in range(len(im)):
    me = i
    for j in range(i + 1, len(im)):
        if im[j] > im[me]:
            me = j
    im[i], im[me] = im[me], im[i]
resultado = []
i, j = 0, 0
for k in range(t):
    if k % 2 == 0:
        resultado.append(pa[i])
        i += 1
    else:
        resultado.append(im[j])
        j += 1

print("vector resultante:", resultado)
            

#8.	Se tiene un vector con datos numéricos, 
# ordenar la mitad del vector en orden ascendente y la otra mitad en orden descendente.
v=[6,10,2,8,7,3,11,17]
t=len(v)
print("vector ingresado : ",v)
mitad=t//2
for i in range(mitad):
    me = i
    for j in range(i + 1, mitad):
        if v[j] < v[me]:
            me = j
    v[i], v[me] = v[me], v[i]

for x in range(mitad,t):
    me = x
    for j in range(x + 1, t):
        if v[j] > v[me]:
            me = j
    v[x], v[me] = v[me], v[x]
print("vector resultante : ",v)

#9.	Se tiene un vector con datos numéricos, formar dos vectores uno con los números pares y 
# otro con los números primos y ordenarlos ascendente y descendente respectivamente
v=[8,12,16,4,7,17,13,29]
pares=[]
primos=[]
for i in range(len(v)):
    if v[i]%2==0:
        pares.append(v[i])
    else:
        r=2
        p=False
        while r<v[i] and p==False:
            if v[i]%r==0:
                p=True
            r+=1
        if p==False:
            primos.append(v[i])
for i in range(len(pares)):
    me=i
    for j in range(i+1, len(pares)):
        if pares[j]<pares[me]:
            me=j
    pares[i],pares[me]=pares[me],pares[i]
for i in range(len(primos)):
    me=i
    for j in range(i+1, len(primos)):
        if primos[j]>primos[me]:
            me=j
    primos[i],primos[me]=primos[me],primos[i]
print("vector ingresado : ",v)
print("vector de pares : ",pares)
print("vector de primos : ",primos)

#10.	Se tiene un vector con datos numéricos ordenados y repetidos, mostrar los números 
# y las veces que se repiten utilizando el concepto de rompimiento de control.
v=[2,2,2,2,5,5,4,4,4,4,4,8]
j=0
i=0
while i<len(v):
    i=j
    aux=v[i]
    g=0
    while j<len(v) and v[j]==aux:
        g=g+1
        j+=1
    print("el numero ",aux," se repite ",g," veces")
    i+=1

#11.	Se tienen dos vectores con datos numéricos, en el primer vector hay números múltiplos 
# de tres que determinan la cantidad de datos de rangos correspondientes al vector dos, encontrar 
# el mayor, el menor y el promedio de cada rango.
rang=[3,6]
v2=[5,8,4,12,4,26,34,17,19,]
j=0
for i in range(len(rang)):
    t=rang[i]
    c=False
    con=0
    suma=0
    while j<t:
        if c==False:
            men=v2[j]
            may=v2[j]
            c=True
        else:
            if v2[j]>may:
                may=v2[j]
            else:
                if v2[j]<men:
                    men=v2[j]
        suma+=v2[j]
        j+=1
        con+=1
    if con>0:
        prom=suma/con
    print("el mayor del rango ",i+1," es el ",may)
    print("el menor del rango ",i+1," es el ",men)
    print("el promedio del rango ",i+1," es ",prom)   

#12.Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.
v=[3,11,12,14,16,8,7,9]
c=[15,16,14,3,9,7,11,3]
n=[]
z=0
for i in range(len(v)):
    r=2
    p=False
    while r<v[i] and p==False:
        if v[i]%r==0:
            p=True
        r+=1
    if p==False:
        k=v[i]
        for j in range(len(c)):
            if k==c[j]:
                if z==0:
                    n.append(k)
                    z=1
                else:
                    x=0
                    for s in range(len(n)):
                        if k==n[s]:
                            x=1
                    if x==0:
                        n.append(k)
print("vector con los primos comunes sin repetirse : ",n)

#13.Se tienen dos vectores con datos numéricos formar un vector con la unión de los Fibonacci sin repetidos
v=[3,11,12,14,16,8,7,9]
c=[15,16,14,3,9,7,11,3]
n=[]
z=0
for i in range(len(v)):
    a=0
    b=1
    t=0
    while t<v[i]:
            t=a+b
            a=b
            b=t
    if t==v[i]:
            if z==0:
                n.append(t)
                z=1
            else:
                x=0
                for s in range(len(n)):
                    if t==n[s]:
                        x=1
                if x==0:
                    n.append(t)
for j in range(len(c)):
    a=0
    b=1
    t=0
    while t<c[j]:
        t=a+b
        a=b
        b=t
    if t==c[j]:
        x=0
        for s in range(len(n)):
            if t==n[s]:
                x=1
        if x==0:
            n.append(t)
print("vector con la union de los fibonacci sin repetirse : ",n)

#14.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente 
# y el otro ordenado descendentemente, formar un tercer vector por mezcla de tal forma 
# que quede ordenado descendentemente.
a=[5,7,12,18,25,31]
b=[37,35,29,19,14]
c=[]
ta=len(a)
tb=len(b)
i=ta-1
j=0
print(i)
while i>=0 and j<tb:
    if a[i]>b[j]:
        c.append(a[i])
        i-=1
    else:
        c.append(b[j])
        j+=1
if i==-1:
    while j<=tb:
        c.append(b[j])
        j+=1
else:
    while i>=0:
        c.append(a[i])
        i-=1
print("vector ordenado por mezcla : ",c)

#15.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente y el 
# otro ordenado descendentemente, formar un tercer vector por mezcla de tal forma que quede 
# ordenado descendentemente, solo con números pares
a=[5,7,12,18,25,31]
b=[37,35,29,19,14]
c=[]
ta=len(a)
tb=len(b)
i=ta-1
j=0
print(i)
while i>=0 and j<tb:
    if a[i]>b[j]:
        if a[i]%2==0:
            c.append(a[i])
        i-=1
    else:
        if b[j]%2==0:
            c.append(b[j])
        j+=1
if i==-1:
    while j<=tb:
        if b[j]%2==0:
            c.append(b[j])
        j+=1
else:
    while i>=0:
        if a[i]%2==0:
            c.append(a[i])
        i-=1
print("vector ordenado por mezcla : ",c)

#16.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, formar un tercer 
# vector con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.
a=[3,5,13,21,15,4,9]
v=[]
x=0
for i in range(len(a)):
    c=0
    b=1
    t=0
    while t<a[i]:
        t=c+b
        c=b
        b=t
    if t==a[i]:
        if x==0:
            g=a[i]
            l=a[i]
            x=1
        else:
            if a[i]>g:
                g=a[i]
            else:
                if a[i]<l:
                    l=a[i]
k=l
while k<=g:
    r=2
    p=False
    while r<k and p==False:
        if k%r==0:
            p=True
        r+=1
    if not p:
        v.append(k)
    k+=1
print("los numeros primos que estan entre el ",l," y el ",g," son : ",v)

#17.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, 
# hallar el promedio de los múltiplos de tres, que están entre el segundo y tercer Fibonacci del vector
a=[1,3,13,5,21,15,4,9]
v=[]
x=1
do=0
dr=0
for i in range(len(a)):
    c=0
    b=1
    t=0
    while t<a[i]:
        t=c+b
        c=b
        b=t
    if t==a[i]:
        if x==2:
            l=a[i]
        else:
            if x==3:
                g=a[i]
        x+=1
if l<g:
    k=l
    while k<=g:
        if k%3==0:
            do+=k
            dr+=1
        k+=1
else:
    k=g
    while k<=l:
        if k%3==0:
            do+=k
            dr+=1
        k+=1
if dr>0:
    prom=do/dr
print("el promedio de los multiplos de 3 que estan entre el ",l," y el ",g," es : ",prom)

#18.	Se tiene un vector con datos numéricos donde hay varios Fibonacci, encontrar el segundo 
# y tercer Fibonacci y sus posiciones, reemplazar las posiciones comprendidas en estos dos valores 
# con el factorial del Fibonacci menor de los dos.
v=[]
x=1
r=1
print("vector ingrasado : ",a)
for i in range(len(a)):
    c=0
    b=1
    t=0
    while t<a[i]:
        t=c+b
        c=b
        b=t
    if t==a[i]:
        if x==2:
            l=a[i]
            pl=i
        else:
            if x==3:
                g=a[i]
                pg=i
        x+=1
if l<g:
    while l>0:
        r*=l
        l-=1
    a.insert(pl, r)
    a.remove(a[pl+1])
    a.insert(pg, r)
    a.remove(a[pg+1])
    
else:
    while g>0:
        r*=g
        g-=1
    a.insert(pl, r)
    a.remove(a[pl+1])
    a.insert(pg, r)
    a.remove(a[pg+1])

print("vector resultante : ",a)
