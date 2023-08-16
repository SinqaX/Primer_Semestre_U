#ALGORITMO EXAMEN
#se tienen dos vectores con datos numerico s, en el primer vector los pimos 2 y 3 determianan la cantidad de datos a 
#recorrer en el segundo vector, hallar el proemedio de los paresque estan en estos dos rangos 
pri=[1,3,2,4,7,2]
pa=[1,2,3,4,6,7,8,9]
c=0
pri_2=0
pri_3=0
for i in range(len(pri)):
    r=2
    p= False
    while r<pri[i]  and p==False:
        if pri[i]%r==0:
            p=True
        r+=1
    if p==False:
        if c==2:
            pri_2=pri[i]
        else: 
            if c==3:
                pri_3=pri[i]
        c+=1
print(pri_2,pri_3)

if pri_2<pri_3:
    lim_inf=pri_2
    lim_sup=pri_3
else:
    lim_inf=pri_3
    lim_sup=pri_2
sump=0
cp=0
j=lim_inf
for j in range(lim_sup):
    if pa[j]%2==0:
        sump+=pa[j]
        cp+=1
if cp>0:
    prom=sump/cp
print("el promedio de numeros pares entre los rangos ",lim_inf," y ",lim_sup," es : ",prom)

