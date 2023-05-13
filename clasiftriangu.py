a = int(input("agregar a : "))
b = int(input("agregar b : "))
c = int(input("agregar c : "))
if a==b:
    if b==c:
        print("es triangulo equilatero")
    else:
       print("es triangulo isoceles")
else:
    if b==c:
          print("triangulo isoceles")
    else:
        if a==c:
           print("triangulo isoceles")
        else:
           print("triangulo escaleno")