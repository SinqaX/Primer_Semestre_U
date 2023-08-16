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













       




        














    





    

    





