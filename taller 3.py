# 17.	Se tiene una matriz cuadrada de orden N realizar lo siguiente
m=[
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
def punto_17_1(m):
    print("-17.1) hallar el promedio diagonal prinpipal y secundadario\n")
    fm=len(m)
    cm=len(m[0])
    sup=0
    for i in range(fm):
        for j in range(cm):
            if i==j :
                sup+=m[i][j]
    prop=sup/fm

    fm=len(m)
    cm=len(m[0])
    sus=0
    s=fm-1
    for i in range(fm):
        for j in range(cm):
            if i+j== s:
                sus+=m[i][j]
    prop=sus/fm
    print(f"el promedio de la daigonal principal es {prop}")
    print(f"el promedio de la daigonal secundaria es {prop}")


def punto_17_2(m):
    print("-17.2) Ordenar ascendentemente la diagonal principal\n")
    fm=len(m)
    cm=len(m[0])
    for i in range(fm):
        for j in range(cm):
            if i==j:
                mei=i
                mej=j
                for k in range(i+1,fm):
                    for l in range(j+1,cm):
                        if k==l:
                            if m[k][l]<m[mei][mej]:
                                mei=k
                                mej=l
                            break
                m[i][j],m[mei][mej]=m[mei][mej],m[i][j]

    print("la diagonal principal ordenada ascendentemente queda asi : \n")  
    for f in m:
        print(f)


#-	Hallar el promedio de los pares que están encima de la diagonal principal y de los 
# impares de la diagonal secundaria
def punto_17_3(m):
    print("-17.3) Hallar el promedio de los pares que están encima de la diagonal principal y de los impares de la diagonal secundaria\n")
    fm=len(m)
    cm=len(m[0])
    su=0
    c=0
    sus=0
    cs=0
    for i in range(fm):
        for j in range(cm):
            if j>i:
                if m[i][j]%2==0:
                    su+=m[i][j]
                    c+=1
            elif i+j==fm:
                if m[i][j]!=2:
                    sus+=m[i][j]
                    cs+=1
    if c>0:
        prom=su/c
        print(f"el promedio de pares por encima de la diagonal principal es : {prom}")
    if cs>0:
        proms=sus/cs
        print(f"el promedio de los numeros impares de la diagonal secundaria es : {proms}")

# -	Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con 
# el Fibonacci mayor.
def punto_17_4(m):
    print("-17.4) Llenar la diagonal principal con el primo menor de la matriz y la diagonal secundaria con el Fibonacci mayor.\n")
        
    fm=len(m)
    cm=len(m[0])
    c=0
    z=0
    for i in range(fm):
        for j in range(cm):
            dato=m[i][j]
            if primo(dato):
                if c==0:
                    pm=m[i][j]
                    c=1
                else:
                    if m[i][j]<pm:
                        pm=m[i][j]
            if fibonacci(dato):
                if z==0:
                    fm=m[i][j]
                    z=1
                else:
                    if m[i][j]>fm:
                        fm=m[i][j]

    for i in range(fm):
        for j in range(cm):
            if i==j:
                m[i][j]=pm
            if i+j==cm-1:
                m[i][j]=fm
    print("matriz resultante : \n")
    for f in m:
        print(f)

# -	Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.
def punto_17_5(m):
    print("-17.5) Llenar el contorno de la matriz con el par mayor de la matriz y la parte interna con el menor de los impares de la matriz.\n")
    fm=len(m)
    cm=len(m[0])
    c=0
    z=0
    for i in range(fm):
        for j in range(cm):
            if m[i][j]%2==0:
                if c==0:
                    p=m[i][j]
                    c=1
                else:
                    if m[i][j]>p:
                        p=m[i][j]
            if m[i][j]%2!=0:
                if z==0:
                    im=m[i][j]
                    z=1
                else:
                    if m[i][j]<im:
                        im=m[i][j]
    for i in range(fm):
        for j in range(cm):
            if i==0 or i==fm-1 or j==0 or j==cm-1:
                m[i][j]=p
            else:
                m[i][j]=im
    print("matriz resultante : \n")
    for f in m:
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
def punto_18_1(m1,m2):
    print("-18.1) Formar un vector con los elementos comunes de las dos matrices sin repetidos\n")
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
def punto_18_2(m1,m2):
    print("-18.2) Formar un vector con los primos comunes de las dos matrices sin repetidos \n")
    fm1=len(m1)
    cm1=len(m1[0])
    fm2=len(m2)
    cm2=len(m2[0])
    z=0
    v=[]
    for i in range(fm1):
        for j in range(cm1):
            valor=m[i][j]
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
def punto_18_3(m1,m2):
    print("-18.3) Formar un vector con los primos no comunes de las dos matrices sin repetidos\n")
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
m=[
    [3, 7, 2, 3],
    [8, 2, 5, 8],
    [1, 6, 1, 4],
    [9, 4, 7, 2],
    [3, 8, 3, 6]
]
def punto_19(m):
    v=[]
    fi=len(m)
    for i in range(fi):
        co=len(m[i])
        for j in range(co):
            aux=m[i][j]
            c=1
            for i in range(fi):
                for l in range(j+1,co):
                        if m[i][l]==aux:
                            c+=1
                            
            dato=c
            if dato > 0 and fibonacci(dato) and dato not in v:
                v.append(dato)
    print(f"vector resultante : {v}")

def Leer_matriz():
    m=[]
    fm=int(input("ingrese la cantidad de filas :"))
    cm=int(input("ingrese la cantidad de columnas :"))
    for i in range(fm):
        fl=[]
        for j in range(cm):
            val=int(input("ingrese el dato de la matriz : "))
            fl.append(val)
        m.append(fl)
