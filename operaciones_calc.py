# Escribe tu código aquí :-)
ln = {}
for item in range(1, 8):
    ln[item] = []
lr = {}
for item in range(1, 8):
    lr[item] = []

while True:
    print("Calculadora")
    print("elija opción de cálculo")
    print("1- Exponente")
    print("2- Modulo")
    print("3- Division entera")
    print("4- Division")
    print("5- Multiplicacion")
    print("6- Sustraccion")
    print("7- Adicion")
    print("0- Salir")
    opcion = input("> ")
    if opcion == "0":
        print("Gracias por usar la super calculadora")
        break
    elif opcion == "1":
        n1 = int(input("Base: "))
        e1 = int(input("Exponente: "))
        ln[1].append([n1, e1])
        resultado1 = n1 ** e1
        lr[1].append(resultado1)
        print("Resultado: ", resultado1)
    elif opcion == "2":
        n1 = int(input("Operando: "))
        n2 = int(input("Operador: "))
        resultado2 = n1 % n2
        ln[2].append([n1, n2])
        lr[2].append(resultado2)
        print("Resultado: ", resultado2)
    elif opcion == "3":
        n1 = int(input("Operando: "))
        n2 = int(input("Operador: "))
        resultado3 = n1 // n2
        ln[3].append([n1, n2])
        lr[3].append(resultado3)
        print("Resultado: ", resultado3)
    elif opcion == "4":
        n1 = int(input("Operando: "))
        n2 = int(input("Operador: "))
        resultado4 = n1 / n2
        ln[4].append([n1, n2])
        lr[4].append(resultado4)
        print("Resultado: ", resultado4)

    elif opcion == "5":
        n1 = int(input("Operando: "))
        n2 = int(input("Operador: "))
        resultado5 = n1 * n2
        ln[5].append([n1, n2])
        lr[5].append(resultado5)
        print("Resultado: ", resultado5)
    elif opcion == "6":
        n1 = int(input("Operando: "))
        n2 = int(input("Operador: "))
        resultado6 = n1 - n2
        ln[6].append([n1, n2])
        lr[6].append(resultado6)
        print("Resultado: ", resultado6)
    elif opcion == "7":
        n1 = int(input("Operando: "))
        n2 = int(input("Operador: "))
        resultado7 = n1 + n2
        ln[7].append([n1, n2])
        lr[7].append(resultado7)
        print("Resultado: ", resultado7)
print("Resumen: ")

print(ln)
for item in ln.values():
    print(item)
print(lr)
for item in lr.values():
    print(item)
