
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

#taller 3


def taller_3_punto_9():
 import random
 m9=[]
 fila=int(input("Inserte cantidad de filas "))
 columna=int(input("Inserte cantidad de columnas "))

 for i in range(fila):
    fila=[]
    for j in range(columna):
        fila.append(random.randint(1,10000))
 
    m9.append(fila)

 print(m9)
 es_primo=0
 print("Los primos en la matriz son ")
 for j in range(columna):
    for i in range(fila):
        c=1
        mv=0
        while c<=m9[i][j]:
            if m9[i][j] % c==0:
                mv+=1
            c+=1

        if mv==2:
            es_primo+=1
            if es_primo==2:
                seg_primo=m9[i][j]
                print(m9[i][j], " es el segundo primo")
                print("Está en c ",j)
                print("y f ",i) 
            elif es_primo==4:
                cto_primo=m9[i][j]
                print(m9[i][j], " es el cuarto primo")
                print("Esta en c ",j)
                print("y f ",i)

 if cto_primo<seg_primo:
    aux=seg_primo
    seg_primo=cto_primo
    cto_primo=aux

 cont=seg_primo+1
 b=0
 while cont < cto_primo and b==0:
    cont2=1
    mv=0
    while cont2<=cont:
        if cont % cont2 ==0:
            mv+=1
        cont2+=1

    if mv==2:
        b+=1
    else:
        cont+=1            

 if b==0:
    print("No hay más primos entre el segundo y cuarto primo, por lo tanto estos son consecutivos")
 else:
    print("Hay números primos entre el tercero y cuarto primo, por lo que no son consevutivos")


def taller_3_punto_10():
 m10 = []
 nf = int(input("cantidad de filas "))
 nc = int(input("cantidad de columnas "))

 for i in range(nf):
    f = []
    for j in range(nc):
        f.append(int(input(f'Dato({i},{j})=')))
    m10.append(f)

 print("Matriz")
 for i in range(nf):
    for j in range(nc):
        print("Fila ",i," y Columna ",j, m10[i][j])

 for j in range(nc):
    if j % 2 == 0: 
        for i in range(nf - 1):
            for k in range(i + 1,nf):
                if m10[k][j] < m10[i][j]:
                    aux = m10[i][j]
                    m10[i][j] = m10[k][j]
                    m10[k][j] = aux
    else: 
        for i in range(nf - 1):
            for k in range(i + 1, nf):
                if m10[k][j] > m10[i][j]:
                    aux = m10[i][j]
                    m10[i][j] = m10[k][j]
                    m10[k][j] = aux

 print("Con datos reordenados ")
 for i in range(nf):
    for j in range(nc):
        print("Fila ",i," Columna ",j ,m10[i][j])


def taller_3_punto_11():
                    #Se tienen dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. (ordenamiento por mezcla).

                    import random

                    def mezclar(vector1, vector2):
                        resultado = []
                        i = j = 0

                        while i < len(vector1) and j < len(vector2):
                            if vector1[i] < vector2[j]:
                                resultado.append(vector1[i])
                                i += 1
                            else:
                                resultado.append(vector2[j])
                                j += 1

                        resultado.extend(vector1[i:])
                        resultado.extend(vector2[j:])
                        return resultado

                    def ordenar_mezcla(vector):
                        if len(vector) <= 1:
                            return vector

                        medio = len(vector) // 2
                        izquierda = vector[:medio]
                        derecha = vector[medio:]

                        izquierda = ordenar_mezcla(izquierda)
                        derecha = ordenar_mezcla(derecha)

                        return mezclar(izquierda, derecha)

                    matriz1 = []
                    matriz2 = []
                    dimensiones = random.randint(3, 6)

                    for i in range(dimensiones):
                        fila_actual = []
                        for j in range(dimensiones):
                            fila_actual.append(random.randint(1, 50))
                        matriz1.append(fila_actual)

                    for i in range(dimensiones):
                        fila_actual = []
                        for j in range(dimensiones):
                            fila_actual.append(random.randint(1, 50))
                        matriz2.append(fila_actual)

                    def mostrar_matriz(matriz):
                        for fila in matriz:
                            print(" ".join("{:4}".format(n) for n in fila))

                    print("\nMatriz 1")
                    mostrar_matriz(matriz1)

                    print("\nMatriz 2")
                    mostrar_matriz(matriz2)

                    # Convertir matrices en listas planas para ordenarlas
                    vector1 = [numero for fila in matriz1 for numero in fila]
                    vector2 = [numero for fila in matriz2 for numero in fila]

                    vector1_ordenado = ordenar_mezcla(vector1)
                    vector2_ordenado = ordenar_mezcla(vector2)

                    print("\nVector 1 ordenado:")
                    print(vector1_ordenado)

                    print("\nVector 2 ordenado:")
                    print(vector2_ordenado)

                    # Combinar y ordenar los dos vectores utilizando el método de mezcla
                    resultado_combinado = mezclar(vector1_ordenado, vector2_ordenado)
                    print("\nResultado combinado y ordenado:")
                    print(resultado_combinado)



def taller_3_punto_12():
        m12=[[2,5,5,3,6],
        [4,5,5,2,6],
        [7,5,7,2,6],
        [7,3,3,4,6],
        [8,8,8,8,9]]
        vp=[]
        nf=5
        nc=5
        for f in m12:
            print(f)
        def promedio_de_cada_fila():
            for i in range(nf):
                psum=0
                for j in range(nc):
                    psum=psum+m12[i][j]
                p=psum/nc 
                vp.append(p)
        promedio_de_cada_fila()
        for i in range(nf):
            for j in range(nc):
                if vp[j]>vp[i]:
                    auxvp=vp[i]
                    vp[i]=vp[j]
                    vp[j]=auxvp
                    for k in range(nc):
                        aux=m12[j][k]
                        m12[j][k]=m12[i][k]
                        m12[i][k]=aux
        print("vector con promedios",vp)
        print("filas de acuerdo al orden ascendente de los promedios de cada fila",m12)


m1_taller_3_punto_14=[[2,5,6,8],
                    [3,5,7,12],
                    [3,11,13,17],
                    [23,20,18,4]]
m2_taller_3_punto_14=[[20,2,5,8],
                    [6,7,7,9],
                    [20,23,4,6],
                    [5,6,4,6]]


def taller_3_punto_14_1():
    nf1=4
    nc1=4
    nf2=4
    nc2=4
    v1=[]
    v1d=0
    for i in range(nf1):
        for j in range(nc1):
            for k in range(nf2):
                for l in range(nc2):
                    if m1_taller_3_punto_14[i][j]==m2_taller_3_punto_14[k][l]:
                        b2=0
                        for n in range(v1d): 
                            if m1_taller_3_punto_14[i][j]==v1[n] and b2==0:
                                b2=1
                        if b2==0:
                            v1.append(m1_taller_3_punto_14[i][j])
                            v1d+=1
    print("vector con los elementos comunes de las dos matrices sin repetidos ",v1)


def taller_3_punto_14_2():
    nf1=4
    nc1=4
    nf2=4
    nc2=4
    v2=[]
    v2d=0
    for i in range(nf1):
        for j in range(nc1):
            b3=0
            c2=2
            if m1_taller_3_punto_14[i][j]<=2:#por si el primo es menor a 2
                for k in range(nf2):
                    for l in range(nc2):
                        if m1_taller_3_punto_14[i][j]==m2_taller_3_punto_14[k][l]:
                            b2=0
                            for n in range(v2d): 
                                if m1_taller_3_punto_14[i][j]==v2[n] and b2==0:
                                    b2=1
                            if b2==0:
                                v2.append(m1_taller_3_punto_14[i][j])
                                v2d+=1 
            if c2<=m1_taller_3_punto_14[i][j]-1 and b3==0:
                if m1_taller_3_punto_14[i][j]%c2==0:
                    b3=1
                else:
                    c2+=1
                if b3==0:
                    for k in range(nf2):
                        for l in range(nc2):
                            if m1_taller_3_punto_14[i][j]==m2_taller_3_punto_14[k][l]:
                                b2=0
                                for n in range(v2d): 
                                    if m1_taller_3_punto_14[i][j]==v2[n] and b2==0:
                                        b2=1
                                if b2==0:
                                    v2.append(m1_taller_3_punto_14[i][j])
                                    v2d+=1
    print("vector con los primos comunes de las dos matrices sin repetidos",v2)


def taller_3_punto_14_3():
    nf1=4
    nc1=4
    nf2=4
    nc2=4
    v3=[]
    v3d=0
    for i in range(nf1):
        for j in range(nc1):
            c2=2
            b=0
            while c2<m1_taller_3_punto_14[i][j]-1 and b==0:
                if m1_taller_3_punto_14[i][j]%c2==0:
                    b=1
                else:
                    c2+=1
            if b==0:
                b6=0
                for k in range(nf2):
                    for l in range(nc2):
                        if m1_taller_3_punto_14[i][j]==m2_taller_3_punto_14[k][l] and b6==0:
                            b6=1
                if b6==0:
                    b5=0
                    for n in range(v3d):
                        if m1_taller_3_punto_14[i][j]==v3[n] and b5==0:
                            b5=1
                    if b5==0:       
                        v3.append(m1_taller_3_punto_14[i][j])
                        v3d+=1
    print("vector con los primos no comunes de las dos matrices sin repetidos",v3)




m15=[[2,5,5,3,6],
   [4,5,5,2,6],
   [7,5,7,2,6],
   [7,3,3,4,6],
   [8,8,8,8,9]]

def taller_3_punto_15():
    nf=5
    nc=5
    va=[]
    vn=[]
    vnd=0
    vad=0
    for i in range(nf):
        for j in range(nc):
            cp=0
            b=0
            for n in range(vnd):
                if m15[i][j]==vn[n] and b==0:
                    b=1
            if b==0:
                vn.append(m15[i][j])
                vnd+=1
                for k in range(nf):
                    for l in range(nc):
                        if m15[i][j]==m15[k][l]:
                            cp+=1
                va.append(cp)
                vad+=1
    print("vector con datos",vn)
    print("contador de datos",va)
    vf=[]
    vaf=0
    for i in range(vad):
        num=va[i]
        if fibonacci(num):
            b1=0
            for j in range(vaf):
                if va[i]==vf[j] and b1==0:
                    b1=1
            if b1==0:
                vf.append(va[i])
                vaf+=1
    print("vector final",vf)




vp=[]
def promedio_de_cada_fila():
    for i in range(nf):
        psum=0
        for j in range(nc):
            psum=psum+m16[i][j]
        p=psum/nc 
        vp.append(p)

m16=[[5,8,10,12,20],
   [3,6,8,11,14],
   [4,17,18,10,15],
   [13,19,18,7,5],
   [21,4,8,7,11]]
nf=5
nc=5
#-Intercambia la primera columna con la última

def taller_3_punto_16_1():
    for i in range(nf):
        for j in range(nc):
            if i==0:
                aux=m16[0][j]
                m16[0][j]=m16[nf-1][j]
                m16[nf-1][j]=aux
    print("primera fila y utima intercambiada",m16)
#-Obtener el mayor, menor y promedio de cada columna
vp=[]

def taller_3_punto_16_2():  
    for i in range(nf):
        psum=0
        men=m16[i][0]
        may=m16[i][0]
        for j in range(nc):
            if m16[i][j]<men:
                men=m16[i][j]      
            elif m16[i][j]>may:
                may=m16[i][j]
            psum=psum+m16[i][j]
        p=psum/nc 
        print("mayor=",may,"menor=",men,"promedio fila=",p)
        
#-Ordenar las filas pares ascendentemente y las filas impares descendentemente

def taller_3_punto_16_3():
    for i in range(nf):
        if i%2==0:
            for j in range(nc):
                for k in range(nc):
                    if m16[i][k]>m16[i][j]:
                        aux=m16[i][j]
                        m16[i][j]=m16[i][k]
                        m16[i][k]=aux
        else:
            for j in range(nc):
                for k in range(nc):
                    if m16[i][k]<m16[i][j]:
                        aux=m16[i][j]
                        m16[i][j]=m16[i][k]
                        m16[i][k]=aux
    print("matriz filas pares ascendentemente y las filas impares descendentemente",m16)
#-Ordenar la matriz descendentemente

def taller_3_punto_16_4():
    for i in range(nf):
        for j in range(nc):
            k=i
            l=j
            for k in range(nf):
                for l in range(nc):
                    if m16[k][l]<m16[i][j]:
                        aux=m16[i][j]
                        m16[i][j]=m16[k][l]
                        m16[k][l]=aux
                l=0
    print("matriz descendentemente",m16)
#-Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila

def taller_3_punto_16_5():
    promedio_de_cada_fila()
    for i in range(nf):
        for j in range(nc):
            if vp[j]>vp[i]:
                auxvp=vp[i]
                vp[i]=vp[j]
                vp[j]=auxvp
                for k in range(nc):
                    aux=m16[j][k]
                    m16[j][k]=m16[i][k]
                    m16[i][k]=aux
    print("vector con promedios",vp)
    print("filas de acuerdo al orden ascendente de los promedios de cada fila",m16)
#-Intercambiar las filas donde se encuentre el mayor y el menor de la matriz

def taller_3_punto_16_6():

    men=m16[0][0]
    may=m16[0][0]
    for k in range(nf):
        for l in range(nc):
            if m16[k][l]<men:
                men=m16[k][l]
                posmen=k
            elif m16[k][l]>may:
                may=m16[k][l]
                posmay=k
    for k in range(nf):
        for l in range(nc):
            aux=m16[posmen][l]
            m16[posmen][l]=m16[posmay][l]
            m16[posmay][l]=aux
    print("filas del mayor y menor intercambiadas",m16)
#-Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el  Fibonacci 4.

def taller_3_punto_16_7():
    cf=0
    pos2=0
    pos4=0
    for i in range(nf):
        for j in range(nc):
            num=m16[i][j]
            if fibonacci(num):
                cf+=1
                if cf==2:
                    pos2=i
                elif cf==4:
                    pos4=i
    for l in range(nc):
        aux=m16[pos2][l]
        m16[pos2][l]=m16[pos4][l]
        m16[pos4][l]=aux
    print("fila del segundo fibonacci",pos2,"fila del cuarto fibonacci",pos4)
    print(m16)

#-Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor

def taller_3_punto_16_8():
    primo_mayor=0
    fibonacci_menor=0
    b2=0
    posfibmen=0
    posprimmay=0
    for i in range(nf):
        for j in range(nc):
            c=2
            b=0
            while c<m16[i][j] and b==0:
                if m16[i][j]%c==0:
                    b=1
                else:
                    c+=1
            if b==0:
                if m16[i][j]>primo_mayor:
                    primo_mayor=m16[i][j]
                    posprimmay=i
            a=0
            bf=1
            cf=0
            while cf<m16[i][j]:
                cf=a+bf
                a=bf
                bf=cf
            if cf==m16[i][j] and b2==0:
                fibonacci_menor=m16[i][j]
                b2=1
            if cf==m16[i][j]:
                if m16[i][j]<fibonacci_menor:
                    fibonacci_menor=m16[i][j]
                    posfibmen=i
    for l in range(nc):
        aux=m16[posfibmen][l]
        m16[posfibmen][l]=m16[posprimmay][l]
        m16[posprimmay][l]=aux
    print("primo mayor",primo_mayor,"fibonacci menor",fibonacci_menor)
    print(m16)

#Determinar si el primo 2 y el primo 4 son consecutivos, es decir, no hay un número primo entre los dos

def taller_3_punto_16_9():
    primo2=0
    primo4=0
    cp=0
    for i in range(nf):
        for j in range(nc):
            num=m16[i][j]
            if primo(num):
                cp+=1
                if cp==2:
                    primo2=m16[i][j]
                elif cp==4:
                    primo4=m16[i][j]
    print("segundo primo es ",primo2,"cuarto primo es ",primo4)
    vpp=[]
    cnvpp=0
    cps=0
    for i in range(primo2,primo4-1):
        vpp.append(primo2+1)
        primo2+=1
        cnvpp+=1
    for i in range(cnvpp):
        num=vpp[i]
        if primo(num):
            cps+=1
    if cps>0:
        print("no son consectivos")
    else:
        print("son consecutivos")





# 17.	Se tiene una matriz cuadrada de orden N realizar lo siguiente
m17=[
    [2,5,6,8],
    [5,8,7,4],
    [9,4,1,3],
    [11,4,10,2]
]
def primo(valor):
        r=2
        p=False
        if valor<=1:
            return False
        else:
            while r<valor-1 and p==False:
                if valor%r==0:
                    p=True
                r+=1
            if p==False:
                return True
            else:
                return False
        
def fibonacci(dato):
    a=0
    b=1
    t=0
    while t<dato:
        t=a+b
        a=b
        b=t
    if t==dato:
        return True
    
# -hallar el promedio diagonal prinpipal y secundadario

def taller_3_punto_17_1(m17):
    print("-17.1) hallar el promedio diagonal prinpipal y secundadario\n")
    for f in m17:
        print(f)
    fm=len(m17)
    cm=len(m17[0])
    sup=0
    for i in range(fm):
        for j in range(cm):
            if i==j :
                sup+=m17[i][j]
    prop=sup/fm

    fm=len(m17)
    cm=len(m17[0])
    sus=0
    s=fm-1
    for i in range(fm):
        for j in range(cm):
            if i+j== s:
                sus+=m17[i][j]
    prop=sus/fm
    print(f"el promedio de la daigonal principal es {prop}")
    print(f"el promedio de la daigonal secundaria es {prop}")


def taller_3_punto_17_2(m17):
    print("-17.2) Ordenar ascendentemente la diagonal principal\n")
    for f in m17:
        print(f)
    fm=len(m17)
    cm=len(m17[0])
    for i in range(fm):
        for j in range(cm):
            if i==j:
                mei=i
                mej=j
                for k in range(i+1,fm):
                    for l in range(j+1,cm):
                        if k==l:
                            if m17[k][l]<m17[mei][mej]:
                                mei=k
                                mej=l
                            break
                m17[i][j],m17[mei][mej]=m17[mei][mej],m17[i][j]

    print("la diagonal principal ordenada ascendentemente queda asi : \n")  
    for f in m17:
        print(f)


#-	Hallar el promedio de los pares que están encima de la diagonal principal y de los 
# impares de la diagonal secundaria
def taller_3_punto_17_3(m17):
    print("-17.3) Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria\n")
    for f in m17:
        print(f)
    fm=len(m17)
    cm=len(m17[0])
    su=0
    c=0
    sus=0
    cs=0
    for i in range(fm):
        for j in range(cm):
            if j>i:
                if m17[i][j]%2==0:
                    su+=m17[i][j]
                    c+=1
            elif i+j==fm:
                if m17[i][j]!=2:
                    sus+=m17[i][j]
                    cs+=1
    if c>0:
        prom=su/c
        print(f"el promedio de pares por encima de la diagonal principal es : {prom}")
    if cs>0:
        proms=sus/cs
        print(f"el promedio de los numeros impares de la diagonal secundaria es : {proms}")

# -	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con 
# el Fibonacci mayor.
def taller_3_punto_17_4(m17):
    print("-17.4) Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.\n")
    for f in m17:
        print(f)  
    fm=len(m17)
    cm=len(m17[0])
    c=0
    z=0
    for i in range(fm):
        for j in range(cm):
            dato=m17[i][j]
            if primo(dato):
                if c==0:
                    pm=m17[i][j]
                    c=1
                else:
                    if m17[i][j]<pm:
                        pm=m17[i][j]
            if fibonacci(dato):
                if z==0:
                    fm=m17[i][j]
                    z=1
                else:
                    if m17[i][j]>fm:
                        fm=m17[i][j]

    for i in range(fm):
        for j in range(cm):
            if i==j:
                m17[i][j]=pm
            if i+j==cm-1:
                m17[i][j]=fm
    print("matriz resultante : \n")
    for f in m17:
        print(f)

# -	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.
def taller_3_punto_17_5(m17):
    print("-17.5) Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.\n")
    for f in m17:
        print(f)
    fm=len(m17)
    cm=len(m17[0])
    c=0
    z=0
    for i in range(fm):
        for j in range(cm):
            if m17[i][j]%2==0:
                if c==0:
                    p=m17[i][j]
                    c=1
                else:
                    if m17[i][j]>p:
                        p=m17[i][j]
            if m17[i][j]%2!=0:
                if z==0:
                    im=m17[i][j]
                    z=1
                else:
                    if m17[i][j]<im:
                        im=m17[i][j]
    for i in range(fm):
        for j in range(cm):
            if i==0 or i==fm-1 or j==0 or j==cm-1:
                m17[i][j]=p
            else:
                m17[i][j]=im
    print("matriz resultante : \n")
    for f in m17:
        print(f)
    
# 18.	Se tienen dos matrices con datos numéricos y se solicita;
m1=[
    [2,5,6,8],
    [5,8,7,4],
    [9,4,1,3],
    [11,4,10,2]
]
m2=[
    [10,7,5,4],
    [9,2,12,9],
    [4,1,11,8],
    [3,15,18,7]
]
# -	Formar un vector con los elementos comunes de las dos matrices sin repetidos
def taller_3_punto_18_1(m1,m2):
    print("-18.1) Formar un vector con los elementos comunes de las dos matrices sin repetidos\n")
    for f in m1:
        print(f)
    for j in m2:
        print(j)
    fm1=len(m1)
    cm1=len(m1[0])
    fm2=len(m2)
    cm2=len(m2[0])
    z=0
    v=[]
    for i in range(fm1):
        for j in range(cm1):
            aux=m1[i][j]
            for k in range(fm2):
                for l in range(cm2):
                    if m2[k][l]==aux:
                        if z==0:
                            v.append(aux)
                            z=1
                        else:
                            if aux not in v:
                                v.append(aux)
    print(f"el vector con los elementos comunes sin repetidos de las dos matrices es : {v}")

# -	Formar un vector con los primos comunes de las dos matrices sin repetidos
def taller_3_punto_18_2(m1,m2):
    print("-18.2) Formar un vector con los primos comunes de las dos matrices sin repetidos \n")
    for f in m1:
        print(f)
    for j in m2:
        print(j)
    fm1=len(m1)
    cm1=len(m1[0])
    fm2=len(m2)
    cm2=len(m2[0])
    z=0
    v=[]
    for i in range(fm1):
        for j in range(cm1):
            valor=m1[i][j]
            if primo(valor):
                aux=valor
                for k in range(fm2):
                    for l in range(cm2):
                        if m2[k][l]==aux:
                            if z==0:
                                v.append(aux)
                                z=1
                            else:
                                if aux not in v:
                                    v.append(aux)
    print(f"el vector resultante con los primos comunes de las matrices es : {v}")

# -	Formar un vector con los primos no comunes de las dos matrices sin repetidos
def taller_3_punto_18_3(m1,m2):
    print("-18.3) Formar un vector con los primos no comunes de las dos matrices sin repetidos\n")
    for f in m1:
        print(f)
    for j in m2:
        print(j)
    fm1=len(m1)
    cm1=len(m1[0])
    fm2=len(m2)
    cm2=len(m2[0])
    v=[]
    for i in range(fm1):
        for j in range(cm1):
            valor=m1[i][j]
            if primo(valor):
                no_es_comun=True
                if valor in m2:
                    no_es_comun=False
                if no_es_comun and valor not in v:
                         v.append(valor)
    print(f"el vector resultante con los primos no comunes de las matrices es : {v}")

#19.	Se tiene una matriz con datos numéricos repetidos, formar un vector con aquellos contadores 
# de datos que se repiten y que sean números Fibonacci, sin repetidos
m19=[
    [3, 7, 2, 3],
    [8, 2, 5, 8],
    [1, 6, 1, 4],
    [9, 4, 7, 2],
    [3, 8, 3, 6]
]

def taller_3_punto_19(m19):
    for f in m19:
        print(f)
    v=[]
    fi=len(m19)
    for i in range(fi):
        co=len(m19[i])
        for j in range(co):
            aux=m19[i][j]
            c=1
            for i in range(fi):
                for l in range(j+1,co):
                        if m19[i][l]==aux:
                            c+=1
                            
            dato=c
            if dato > 0 and fibonacci(dato) and dato not in v:
                v.append(dato)
    print(f"vector resultante : {v}")


def parcial_1_punto_1():   
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

 
def parcial_1_punto_2():
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
            else:
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


def parcial_1_punto_3():
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

 
def parcial_1_punto_4():
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


def parcial_2_punto_1():
    i=0
    dat=int(input("ingrese el dato"))
    while dat!=-5:
        aux=dat
        c=0
        while aux==dat:
            c+=1
            dat=int(input("ingrese el dato"))
        if i==0:
            mayor=c
            menor=c
            i=1
        else:
            if c>mayor:
                mayor=c
            elif c<menor:
                menor=c
    j=0
    suma=0
    while j<menor:
        suma+=mayor
        j+=1
    print("-5 es el numero para salir")
    print("la mulriplicacion de la cantidad del dato mas repetido y menos repetido es: ",suma)


def parcial_2_punto_2():
    v1=[6,5,3,3,5,9,12,15,6]
    v2=[18,6,7,5,3,2,11,20,17]
    vfi=[]
    vtr=[]
    p=False
    print(v1)
    print(v2)
    for i in range(len(v1)):
        a=0
        b=1
        t=0
        while t<v1[i]:
            t=a+b
            a=b
            b=t
            if t==v1[i]:
                aux=v1[i]
                if p==False:
                    vfi.append(aux)
                    p=True
                else:
                    z=0
                    for j in range(len(vfi)):
                        if aux==vfi[j]:
                            z=1
                    if z==0:
                        vfi.append(aux)
    for k in range(len(v2)):
        a=0
        b=1
        t=0
        while t<v2[k]:
            t=a+b
            a=b
            b=t
        if t==v2[k]:
            aux=v2[k]
            c=0
            for j in enumerate(vfi):
                if aux==vfi[j]:
                    c=1
            if c==0:
                vfi.append(aux)
    m=0
    for i in range(len(v1)):
        if v1[i]%3==0:
            if v1[i]%5!=0:
                aux=v1[i]
                for j in range(len(v2)):
                    if aux==v2[j]:
                        if m==0:
                            vtr.append(aux)
                            m=1
                        else:
                            e=0
                            for n in range(len(vtr)):
                                if aux==vtr[n]:
                                    e=1
                            if e==0:
                                vtr.append(aux)
    print("vector fibonaccis: ",vfi)
    print("vector x3 pero no x5: ",vtr)


def parcial_2_punto_3():
 v1p3=[4,2,4,3,4,6,4,8,8,9,11,13,31]
 v2p3=[7,2,9,4,1,6,5,5,14,20,30,40,1,7,6]
 c=0
 for i in range(len(v1p3)):
    a=0
    b=1
    t=0
    while t <v1p3[i]:
        t=a+b
        a=b
        b=t
    if t == v2p3[i]:
        c+=1
        if c==3:
            tf=v1p3[i]
 for i in range (tf):
    me=i
    for j in range (i+1, tf):
        if v2p3[j]<v2p3[me]:
            me=j
    v2p3[i], v2p3[me]=v2p3[me], v2p3[i]
    t=len(v2p3)
    for k in range (tf, t):
        ma=k
        for n in range (k+1, t):
            if v2p3[n]>v2p3[ma]:
                ma=n
    v2p3[k],v2p3[ma]=v2p3[ma],v2p3[k]

def quizz():
 mquizz=[]
 vquizz=[]
 fm=int(input("ingresar fila de la matriz "))
 cm=int(input("ingresa número de columnas en la matriz "))
 t=int(input("ingresar cantidad de datos del vector "))
 c=0
 primo=0
 for k in range(t):
    val=int(input("ingresar el dato del vector"))
    vquizz.append(val)

 for i in range (fm):
    fila=[]
    for j in range(cm):
        val=int(input("ingrese valor de la matriz"))
        fila.append(val)
    mquizz.append(fila)
 for k in range(t):
    z=False
    r=2


    while r < vquizz [k] and z==False:
        if vquizz[k]%r==0:
            z=True
            r+=1
    if z==False:
        primo=r[k]
        for i in range (fm):
            for j in range (cm):
                if primo== mquizz[i][j] and c<2:
                    if c==0:
                        pp=1
                        c=c+1
                    else:
                        if c==1:
                            ps=i
                            c=c+2
 aux=mquizz[pp]
 mquizz[pp]=mquizz[ps]
 mquizz[ps]=aux

 print("matríz resultante ")
 for fila in mquizz:
    print(fila)

def menu_inicio():
    while True:
        respuesta = int(input("""<========MENU========>:
    1. Taller  N° 1
    2. Taller  N° 2
    3. Taller  N° 3                
    4. Parcial N° 1
    5. Parcial N° 2
    6. Quiz                 
    7. Salir
                              Digite su opcion=>    """))
        if respuesta == 1:
            respuesta_taller_1 = int(input("""Qué Punto desea ver a continuación:  
                                           
                                            22. Promedio pares primo mayor y fibonacci menor
                                            23. Promedio factorial impares entre primo mayor y fibonacci menor
                                            24. Encontrar primo y fibonacci a la vez
                                            25. Veces que se repite el segundo primo
                                            26. Determinar triangulo equilatero, escaleno o isóceles
                                           
                                           Digite su opcion=>   """))
            if respuesta_taller_1 == 22:
                taller_1_punto_22()
            if respuesta_taller_1 == 23:
                taller_1_punto_23()
            if respuesta_taller_1 == 24:
                taller_1_punto_24()            
            if respuesta_taller_1 == 25:
                taller_1_punto_25()
            if respuesta_taller_1 == 26:
                taller_1_punto_26()
        if respuesta == 2:
            respuesta_taller_2 = int(input("""Qué Punto desea ver a continuación:
                                            9. Ordenar pares y primos
                                            10. Mostrar repeticiones
                                            11. Multiplos de 3 y rangos correspondientes
                                            12. Vector con primos comunes sin repetidos
                                            13. Vector con fibonaccis comunes sin repetidos
                                            14. Formar un tecer vector que quede ordenado
                                            15. Formar un tercer vector que quede ordenado solo con pares
                                            16. Vector con primos entre fibonacci mayor y menor
                                            17. Promedio multiplos de 3 entre segundo y tercer fibonacci
                                            18. Segundo, tecer fibonacci y sus posiciones, remplazarlas
                                           
                                            Digite su opcion=>   """))
            if respuesta_taller_2 == 9:
                taller_2_punto_9()
            if respuesta_taller_2 == 10:
                taller_2_punto_10()
            if respuesta_taller_2 == 11:
                taller_2_punto_11()
            if respuesta_taller_2 == 12:
                taller_2_punto_12()
            if respuesta_taller_2 == 13:
                taller_2_punto_13()
            if respuesta_taller_2 == 14:
                taller_2_punto_14()
            if respuesta_taller_2 == 15:
                taller_2_punto_15()
            if respuesta_taller_2 == 16:
                taller_2_punto_16()
            if respuesta_taller_2 == 17:
                taller_2_punto_17()
            if respuesta_taller_2 == 18:
                taller_2_punto_18()
        if respuesta == 3:
            respuesta_taller_3 = float(input("""Escoja el punto que desea ver acontinuación: 
                                             
    9.	Se tiene una matriz con datos numéricos, donde hay varios primos, determinar si el segundo primo encontrado al recorrer la matriz
        por columnas es consecutivo con el cuarto primo encontrado.

    10.	Ordenar las columnas pares ascendentemente y las columnas impares descendentemente

    11.	Se tienen dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente con la mezcla de los dos anteriores. (ordenamiento por mezcla).

    12.	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila

    13.solo enunciado= >	Se tiene una matriz cuadrada de orden N realizar lo siguiente
    13.1	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
    13.2	Ordenar ascendentemente la diagonal principal
    13.3	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
    13.4	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fi0bonacci mayor.
    13.5	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

    14.solo enunciado= >	Se tienen dos matrices con datos numéricos y se solicita;
    14.1	Formar un vector con los elementos comunes de las dos matrices sin repetidos
    14.2	Formar un vector con los primos comunes de las dos matrices sin repetidos
    14.3	Formar un vector con los primos no comunes de las dos matrices sin repetidos

    15.	Se tiene una matriz con datos numéricos repetidos, formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos

    16. solo enunciado= >	Se tiene una matriz con datos numéricos y se solicita
    16.1	Intercambia la primera columna con la última
    16.2	Obtener el mayor, menor y promedio de cada columna
    16.3	Ordenar las filas pares ascendentemente y las filas impares descendentemente
    16.4	Ordenar la matriz descendentemente
    16.5	Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila
    16.6	Intercambiar las filas donde se encuentre el mayor y el menor de la matriz
    16.7	Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el  Fibonacci 4.
    16.8	Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor
    16.9	Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos 


    17. solo enunciado= >	Se tiene una matriz cuadrada de orden N realizar lo siguiente
    17.1	Hallar el promedio de la diagonal principal y el promedio de la diagonal secundaria
    17.2	Ordenar ascendentemente la diagonal principal
    17.3	Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria
    17.4	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.
    17.5	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.

    18. solo enunciado= >	Se tienen dos matrices con datos numéricos y se solicita;
    18.1	Formar un vector con los elementos comunes de las dos matrices sin repetidos
    18.2	Formar un vector con los primos comunes de las dos matrices sin repetidos
    18.3	Formar un vector con los primos no comunes de las dos matrices sin repetidos

    19.	Se tiene una matriz con datos numéricos repetidos, formar un vector con aquellos contadores de datos que se repiten y que sean números Fibonacci, sin repetidos
        
    Digite su opcion=>   """))      
            if respuesta_taller_3 == 9:
                taller_3_punto_9()
            if respuesta_taller_3 == 10:
                taller_3_punto_10()
            if respuesta_taller_3 == 11:
                taller_3_punto_11()
            if respuesta_taller_3 == 12:
                taller_3_punto_12()
            if respuesta_taller_3 == 13.1:
                taller_3_punto_17_1(m17)
            if respuesta_taller_3 == 13.2:
                taller_3_punto_17_2(m17)
            if respuesta_taller_3 == 13.3:
                taller_3_punto_17_3(m17)
            if respuesta_taller_3 == 13.4:
                taller_3_punto_17_4(m17)
            if respuesta_taller_3 == 13.5:
                taller_3_punto_17_5(m17)
            if respuesta_taller_3 == 14.1:
                taller_3_punto_14_1()
            if respuesta_taller_3 == 14.2:
                taller_3_punto_14_2()
            if respuesta_taller_3 == 14.3:
                taller_3_punto_14_3()
            if respuesta_taller_3 == 15:
                taller_3_punto_15()
            if respuesta_taller_3 == 16.1:
                taller_3_punto_16_1()
            if respuesta_taller_3 == 16.2:
                taller_3_punto_16_2()
            if respuesta_taller_3 == 16.3:
                taller_3_punto_16_3()
            if respuesta_taller_3 == 16.4:
                taller_3_punto_16_4()
            if respuesta_taller_3 == 16.5:
                taller_3_punto_16_5()
            if respuesta_taller_3 == 16.6:
                taller_3_punto_16_6()
            if respuesta_taller_3 == 16.7:
                taller_3_punto_16_7()
            if respuesta_taller_3 == 16.8:
                taller_3_punto_16_8()
            if respuesta_taller_3 == 16.9:
                taller_3_punto_16_9()
            if respuesta_taller_3 == 17.1:
                taller_3_punto_17_1(m17)
            if respuesta_taller_3 == 17.2:
                taller_3_punto_17_2(m17)
            if respuesta_taller_3 == 17.3:
                taller_3_punto_17_3(m17)
            if respuesta_taller_3 == 17.4:
                taller_3_punto_17_4(m17)
            if respuesta_taller_3 == 17.5:
                taller_3_punto_17_5(m17)
            if respuesta_taller_3 == 18.1:
                taller_3_punto_18_1(m1,m2)
            if respuesta_taller_3 == 18.2:
                taller_3_punto_18_2(m1,m2)
            if respuesta_taller_3 == 18.3:
                taller_3_punto_18_3(m1,m2)
            if respuesta_taller_3 == 19:
                taller_3_punto_19(m19)
        if respuesta == 4:
            respuesta_parcial_1 = int(input("""Escoja un punto
                                            
                                            UNIVERSIDAD DE NARIÑO
                                            FACULTAD DE INGENIERIA
                                            INGENIERÍA DE SISTEMAS
                                            PROGRAMACION DE COMPUTADORES
                                            EVALUACIÓN 1  24%
                                            
                                            1.   Se tiene una cantidad de números dada, determinar el primo mayor, el Fibonacci menor,
                                            el par menor y realizar la multiplicación de ellos con sumas.25%
                                            2.   Se tiene una cantidad de números dada donde hay varios números que se repiten.
                                            Encontrar el número de veces que se repite el segundo Fibonacci (en orden de entrada)
                                            y determinar si este contador es un número primo. 25%
                                            3.   Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de
                                            triángulos, determinar cuántos triángulos equiláteros, escalenos e isósceles se encuentran
                                            en estos y si la suma de los perímetros de los triángulos equiláteros, es un número Fibonacci. 25%
                                            4.	Se tiene una cantidad de números dada, encontrar los tres primeros Fibonacci de acuerdo
                                            al orden de entrada y determinar el promedio de los números pares
                                            que están entre el mayor y el menor de estos Fibonacci. 25%
                                            
                                            digite la opcion =>"""))
            if respuesta_parcial_1 == 1:
                parcial_1_punto_1()
            if respuesta_parcial_1 == 2:
                parcial_1_punto_2()
            if respuesta_parcial_1 == 3:
                parcial_1_punto_3()
            if respuesta_parcial_1 == 4:
                parcial_1_punto_4()
        if respuesta == 5:
            respuesta_parcial_2 = int(input("""Escoja un punto
                                            
                                            UNIVERSIDAD DE NARIÑO
                                            FACULTAD DE INGENIERIA
                                            INGENIERÍA DE SISTEMAS
                                            PROGRAMACION DE COMPUTADORES
                                            EVALUACIÓN 2  24%
                                            
                                                1.	Se tiene varios datos numéricos repetidos y agrupados  donde el último dato es un -5,
                                                realizar los siguiente, hallar la multiplicación con sumas, de la cantidad de datos del grupo
                                                que más se repite por la cantidad de datos del grupo que menos se repite

                                                2.	Se tienen dos vectores con datos numéricos donde hay varios repetidos, formar dos vectores asi:
                                                Vector 1 con la unión de solo números Fibonacci sin repetidos, sin tener en cuenta aquellos Fibonacci que sean comunes.
                                                Vector 2 con los múltiplos de 3 comunes, que no sean múltiplos de 5

                                                3.	Se tienen dos vectores con datos numéricos, donde el tercer Fibonacci del vector uno determina
                                                la cantidad de datos a tener en cuenta en el vector dos, formando dos rangos un rango con la cantidad
                                                de datos que establece el Fibonacci y el rango dos con el resto, ordenar el primer rango en orden
                                                ascendente y el segundo en orden descendente 
                                                
                                            digite la opcion =>"""))
            if respuesta_parcial_2 == 1:
                parcial_2_punto_1()
            if respuesta_parcial_2 == 2:
                parcial_2_punto_2()
            if respuesta_parcial_2 == 3:
                parcial_2_punto_3()
        if respuesta == 6:
            quizz()
        if respuesta == 7:
            print("se termino")
            break
    menu_inicio()
menu_inicio()
