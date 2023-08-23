##se tiene una matriz cuadrada de orden n realizar lo siguiente 
#-hallar el promedio diagonal prinpipal y secundadario
m=[
    [2,5,6,8],
    [5,8,7,4],
    [9,4,1,3],
    [11,4,10,2]
]
def Promedio_diag_principal(m):
    fm=len(m)
    cm=len(m[0])
    sup=0
    for i in range(fm):
        for j in range(cm):
            if i==j :
                sup+=m[i][j]
    prop=sup/fm
    return  print(f"el promedio de la daigonal principal es {prop}")

def Promedio_diag_Secundaria(m):
    fm=len(m)
    cm=len(m[0])
    sus=0
    s=fm-1
    for i in range(fm):
        for j in range(cm):
            if i+j== s:
                sus+=m[i][j]
    prop=sus/fm
    return  print(f"el promedio de la daigonal secundaria es {prop}")

















       




        














    





    

    





