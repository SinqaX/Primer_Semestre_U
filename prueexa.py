cd = int(input("Ingrese la cantidad de números: "))
c = 1
cp = 0
cn = 1
ce = 0
ctm = 0
xt = 0
ct = 0

while cn <= cd:
    num = int(input("Ingrese el número: "))
    c = 1
    ce = 0
    
    while c <= num:
        if num % c == 0:
            ce = ce + 1
        c = c + 1

    if ce == 2:
        cp = cp + 1
    
    if num % 3 == 0:
        ct = ct + 1
     
    cn = cn + 1

print("La cantidad de números primos es", cp, "y la cantidad de múltiplos de 3 es", ct, "y las tablas de multiplicar de números pares entre estos dos números son:")
if cp < ct:
    ctm = cp
    
    while ctm <= ct:
         if ctm % 2 == 0: 
          print("TABLA DEL", ctm)
          while xt < 11:
            r = ctm * xt
            print(ctm, "x", xt, "=", r)
            xt = xt + 1
            
         ctm = ctm + 1
         xt = 1
else:
    ctm = ct
    
    while ctm <= cp:
        if ctm % 2 == 0:
         print("TABLA DEL", ctm)
         while xt < 11:
          r = ctm * xt
          print(ctm, "x", xt, "=", r)
          xt = xt + 1
            
         ctm = ctm + 1
         xt = 1