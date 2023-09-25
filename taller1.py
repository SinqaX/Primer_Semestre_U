def taller_1_punto_22():
    nd=int(input("Número de datos "))
    cont=1
    es_prim=0
    es_fib=0
    while cont<=nd:
        dato=int(input("Ingresar dato "))
        cont2=1
        mv=0
        while cont2<=dato:
            if dato%cont2 == 0:
                mv+=1
            cont2+=1
        if mv==2:
            es_prim+=1   
            if es_prim==1:
                primay=dato
            elif dato>primay:
                primay=dato

        a=0
        b=1
        t=0
        while t<dato:
            t=a+b
            a=b
            b=t
        if dato==t:
            es_fib+=1
            if es_fib==1:
                fibmen=dato
            elif dato<fibmen:
                fibmen=dato
        cont+=1
    print("El primo mayor y fibonacci menor son ",primay, fibmen)
    if primay<fibmen:
        aux=fibmen
        fibmen=primay
        primay=aux

    psum=0
    npares=0
    cont3=fibmen+1
    print("Numeros pares entre estos dos datos: ")
    while cont3<primay:
        if cont3 % 2==0:
            print(cont3)
            psum+=cont3
            npares+=1
        cont3+=1

    if npares>0:
        prom=psum/npares
        print("Promedio de pares entre el fibonacci menor y el primo mayor es ", prom)
    else:
        print("Sin números pares entre el fibonacci menor y el primo mayor")


def taller_1_punto_23():
    nd=int(input("Cantidad de datos: "))
    cont=1
    es_prim=0
    es_fib=0
    while cont<=nd:
        dato=int(input("Ingrese dato "))
        cont2=1
        mv=0
        while cont2<=dato:
            if dato%cont2==0:
                mv+=1
            cont2+=1
        if mv==2:
            es_prim+=1   
            if es_prim==1:
                primay=dato
            elif dato>primay:
                primay=dato
        a=0
        b=1
        t=0

        while t<dato:
            t=a+b
            a=b
            b=t
        if dato==t:
            es_fib+=1
            if es_fib==1:
                fibmen=dato
            elif dato<fibmen:
                fibmen=dato
        cont+=1
    print(primay," es el primo mayor ",fibmen, "es el fibonacci menor")
    if primay<fibmen:
        aux=fibmen
        fibmen=primay
        primay=aux

    sfac=0
    nfac=0
    cont2=fibmen+1
    while cont2<primay:
        if cont2 % 2!= 0:
            c=cont2
            nfac=1
            while c>0:
                nfac*=c
                c-=1
            print("El impar ",cont2)    
            sfac+=nfac
            nfac+=1
        cont2+=1    
    if nfac>0:
        prom=sfac/nfac
        print("Factoriales de los impares promediados ",prom)
    else:
        print("Sin impares entre el fibonacci menor y el primo mayor")


def taller_1_punto_24():
    cd=int(input("digitar cantidad de numeros a analizar"))
    suma=0
    c=0
    for i in range(1,cd+1):
        num=int(input("digitar dato"))
        if fibonacci(num):
            if primo(num):
                suma+=num
                c+=1
    p=suma/c
    print("promedio de los numeros qque son fibonacci y primos a la vez:",p)


def taller_1_punto_25():
    cd=int(input("digitar cantidad de numeros a analizar"))
    cp=0
    ca=0
    aux=0
    for i in range(1,cd+1):
        num=int(input("digitar dato"))
        if primo(num):
            cp+=1
            if cp==2:
                aux=num
        if num==aux:
            ca+=1
    print("las veces que se repite el segundo primo es:",ca)


def taller_1_punto_26():
    print("""-	  Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes 
    a los lados de triángulos, determinar cuántos triángulos equiláteros, escalenos e isósceles 
    se encuentran en estos triángulos y la suma de los triángulos isósceles Sin utilizar condiciones compuestas.""")

    ct=int(input("ingrese la cantidad de ternas a digitar : "))
    se=0
    si=0
    ses=0
    for i in range(ct):
        print(f"\nTerna N° {i+1}")
        a=int(input("ingrese el valor a : "))
        b=int(input("ingrese el valor b : "))
        c=int(input("ingrese el valor c : "))
        if a == b == c:
            se += 1
        elif a == b or a == c or b == c:
            si += 1
        else:
            ses += 1
    print(f"\ntriangulos equialteros : {se}")
    print(f"triangulos isoceles : {si}")
    print(f"triangulos escalenos : {ses}\n")


def taller_2_punto_9():
    print("""9.	Se tiene un vector con datos numéricos, formar dos vectores uno con los números pares y 
    otro con los números primos y ordenarlos ascendente y descendente respectivamente\n""")
    v=[8,12,16,4,7,17,13,29]
    pares=[]
    primos=[]
    print(v)
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



def taller_2_punto_10():
    print("""10.	Se tiene un vector con datos numéricos ordenados y repetidos, mostrar los números 
    y las veces que se repiten utilizando el concepto de rompimiento de control.\n""")
    v=[2,2,2,2,5,5,4,4,4,4,4,8]
    j=0
    i=0
    print(v)
    while i<len(v):
        i=j
        aux=v[i]
        g=0
        while j<len(v) and v[j]==aux:
            g=g+1
            j+=1
        print("el numero ",aux," se repite ",g," veces")
        i+=1


def taller_2_punto_11():
    print("""11.	Se tienen dos vectores con datos numéricos, en el primer vector hay números múltiplos 
    de tres que determinan la cantidad de datos de rangos correspondientes al vector dos, encontrar 
    el mayor, el menor y el promedio de cada rango.\n""")
    rang=[3,6]
    v2=[5,8,4,12,4,26,34,17,19,]
    j=0
    print(f"""vector rango : {rang}
              vector 2 : {v2}""")
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


def taller_2_punto_12():
    print("""12.Se tienen dos vectores con datos numéricos formar un vector con los primos comunes sin datos repetidos.\n""")
    v=[3,11,12,14,16,8,7,9]
    c=[15,16,14,3,9,7,11,3]
    n=[]
    z=0
    print(f"""vector 1: {v}
        vector 2: {c}""")
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


def taller_2_punto_13():
    print("""13.Se tienen dos vectores con datos numéricos formar un vector con la unión de los Fibonacci sin repetidos\n""")
    v=[3,11,12,14,16,8,7,9]
    c=[15,16,14,3,9,7,11,3]
    n=[]
    z=0
    print(f"""vector 1: {v}
             vector 2: {c}""")
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


def taller_2_punto_14():
    print("""14.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente 
    y el otro ordenado descendentemente, formar un tercer vector por mezcla de tal forma 
    que quede ordenado descendentemente.\n""")
    a=[5,7,12,18,25,31]
    b=[37,35,29,19,14]
    c=[]
    ta=len(a)
    tb=len(b)
    i=ta-1
    j=0
    print(a)
    print(b)
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


def taller_2_punto_15():
    print("""15.	Se tiene dos vectores con datos numéricos, el uno ordenado ascendentemente y el 
    otro ordenado descendentemente, formar un tercer vector por mezcla de tal forma que quede 
    ordenado descendentemente, solo con números pares\n""")
    a=[5,7,12,18,25,31]
    b=[37,35,29,19,14]
    c=[]
    ta=len(a)
    tb=len(b)
    i=ta-1
    j=0
    print(a)
    print(b)
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


def taller_2_punto_16():
    print("""16.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, formar un tercer 
    vector con los números primos que están entre el Fibonacci mayor y el Fibonacci menor.""")
    a=[3,5,13,21,15,4,9]
    v=[]
    x=0
    print(a)
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


def taller_2_punto_17():
    print("""17.	Se tienen un vector con datos numéricos donde hay varios números Fibonacci, 
    hallar el promedio de los múltiplos de tres, que están entre el segundo y tercer Fibonacci del vector\n""")
    a=[1,3,13,5,21,15,4,9]
    v=[]
    x=1
    do=0
    dr=0
    print(a)
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


def taller_2_punto_18():
    print("""18.	Se tiene un vector con datos numéricos donde hay varios Fibonacci, encontrar el segundo 
    y tercer Fibonacci y sus posiciones, reemplazar las posiciones comprendidas en estos dos valores 
    con el factorial del Fibonacci menor de los dos.\n""")
    a=[1,3,13,5,21,15,4,9]
    v=[]
    x=1
    r=1
    print(a)
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