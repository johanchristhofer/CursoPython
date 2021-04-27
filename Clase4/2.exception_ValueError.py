while True:
    try:
        numero = int(input("Ingresa un número: "))
        break  # Rompe el código para que no siga la iteración
    except ValueError:
        print("El dato ingresado no es un número")