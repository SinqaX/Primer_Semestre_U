n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
n3 = int(input("Digite n3: "))

if n1 > n2:
    if n1 > n3:
        print(n1, "es mayor que todos")
    else:
        print(n3, "es mayor que todos")
else:
    if n2 > n3:
        print(n2, "es mayor que todos")
    else:
        print(n3, "es mayor que todos")