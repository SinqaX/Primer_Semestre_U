#se tienen dos listas con datos numericos forar una tercera lista on lo primos no comunes sin repetidos 
#y otra lista con lo s impares comenes sin repetidos la primera lista ordenada ascendente y la otra descendente 
lista_1=[1,5,2,7,11,13]
lista_2=[19,5,4,7,3,3,5]
lista_primos=[]
lista_impares=[]
def es_primo(valor):
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
def es_impar(dato):
    if dato % 2 == 0:
        return False
    else:
        return True
def quick_sort_ascending(lista, inicio, fin):
    if inicio > fin:
        return
    anterior = inicio
    posterior = fin
    pivo = lista[inicio]

    while anterior < posterior:
        while anterior < posterior and lista[posterior] > pivo:
            posterior = posterior - 1

        if anterior < posterior:
            lista[anterior] = lista[posterior]
            anterior = anterior + 1

        while anterior < posterior and lista[anterior] <= pivo:
            anterior = anterior + 1

        if anterior < posterior:
            lista[posterior] = lista[anterior]
            posterior = posterior - 1

        lista[anterior] = pivo

    quick_sort_ascending(lista, inicio, anterior - 1)
    quick_sort_ascending(lista, anterior + 1, fin)
def descendente(lista):
    for i in range(len(lista)):
        me=i
        for j in range(i+1, len(lista)):
            if lista[j]>lista[me]:
                me=j
        lista[i],lista[me]=lista[me],lista[i]

for i in range(len(lista_1)):
    if es_primo(lista_1[i]):
        if lista_1[i] not in lista_2:
            if lista_1[i] not in lista_primos:
                lista_primos.append(lista_1[i])           
    if es_impar(lista_1[i]):
        if lista_1[i] in lista_2:
            if lista_1[i] not in lista_impares:
                lista_impares.append(lista_1[i])
for p in range(len(lista_2)):
    if es_primo(lista_2[p]):
        if lista_2[p] not in lista_1:
            if lista_2[p] not in lista_primos:
                lista_primos.append(lista_2[p]) 
print(f"lista de primos : {lista_primos}")
print(f"lista de impares :{lista_impares}")
quick_sort_ascending(lista_primos, 0, len(lista_primos)-1)
descendente(lista_impares)
print(f"la lista de primos ordenada ascendente queda : {lista_primos}")
print(f"la lista de impares ordenada descendente queda : {lista_impares}")


