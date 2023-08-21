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
    
def CrearMatriz():
    m=[]
    fm=int(input("ingrese la cantidad de filas de la matriz"))
    cm=int(input("ingrese la cantidad de columnas de la matriz"))
    for i in range(fm):
        f=[]
        for j in range(cm):
            val=int(input("ingrese el dato :"))
            f.append(val)
        m.append(f)
    return m
                        
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

def listas(m):
    lp=[]
    lf=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if fibbonaci(m[i][j])==True:
                lf.append(m[i][j])
            if primo(m[i][j])==True:
                lp.append(m[i][j])
    return lp, lf

m=CrearMatriz()
lp,lf=listas(m)
print("vector de fibbonaci :\n",lf)
print("vector de primos : \n",lp)
      


















       




        














    





    

    





