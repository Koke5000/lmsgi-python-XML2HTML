def menu():
    opcion = 0
    while opcion != 3:
        print("\n\nSelecciona la opcion\n1)Leer\n2)Escribir\n3)Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            leer()
        elif opcion == 2:
            escribir()


def leer():
    print("Contenido de file.txt:")
    file = open('data/file.txt')
    lineas = file.readlines()
    for linea in lineas:
        print(linea)


def escribir():
    texto = input("Que quieres poner dentro de file.txt? ")
    file = open('data/file.txt', 'w')
    file.write(texto)


menu()
