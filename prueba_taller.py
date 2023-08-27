# -	  Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes 
# a los lados de triángulos, determinar cuántos triángulos equiláteros, escalenos e isósceles 
# se encuentran en estos triángulos y la suma de los triángulos isósceles Sin utilizar condiciones compuestas.
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


                                



        
















       




        














    





    

    





