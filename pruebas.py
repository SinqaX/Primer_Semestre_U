#FIBONNACCI MENOR VECTOR
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

