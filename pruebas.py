n=[]
c=[]
fn=int(input("ingrese la cantidad de estudiantes : "))
cn=int(input("ingrese la cantidad de notas por estudiante : "))

x=1
for k in range(fn):
    cod=int(input("ingrese el codigo del estudiante  = "))
    c.append(cod)
    x+=1
for i in range(fn):
    fila=[]
    print("ingrese las notas del  estudiante ",c[i])
    s=0
    for j in range(cn-1):
        nota=float(input("ingrese la notas del estudiante = "))
        s+=fila[nota]
        if j==0:
            nota=nota*0.4
        else:
            if j==1:
                nota=nota*0.3
            else:
                if j==2:
                    nota=nota*0.3
        fila.append(nota)
        s+=fila[nota]
    n.append(fila)
    fila.append(s)

for i in range(fn-1):
    for k in range(i+1,cn):
        if n[k][3]>n[i][3]:
            pe=i
            pa=k
        aux=n[pe]
        n[pe]=n[pa]
        n[pa]=aux
        caux=c[pe]
        c[pe]=c[pa]
        c[pa]=caux
for i in range(fn):
    print("Codigo del Estudiante : ",c[i])
    j=1
    while j<cn:
        print("Nota ",j," = ",n[i][j])
        j+=1
    print("Nota final : ",n[i][j])




