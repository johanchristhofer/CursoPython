# Realizar un programa que e permita validar el nivel de seguridad de una contraseña
minuscula = False
mayuscula = False
numero = False
espacio = False
longitud = False

#Realizar un programa que permita validar el nivel de seguridad de una contraseña
#Ingreso un dato desde terminal
password = input('Ingresa tu contraseña: ')

for caracter in password:
    if caracter.islower() == True:
        minuscula = True
    if caracter.isupper() == True:
        mayuscula = True
    if caracter.isdigit() == True:
        numero = True
    if caracter.isspace() == True:
        espacio = True
#print(str(minuscula) + str(mayuscula) + str(numero) + str(espacio))

if espacio == True:
    print('La contraseña no debe tener un espacio')

if len(password) < 8:
    print('La contraseña debe tener minimo 8 caracteres')
    longitud = False
else:
    longitud = True

if minuscula == True and mayuscula == True and numero == True and espacio == False and longitud == True:
    print('La contraseña es valida')
else:
    print('Error la contraseña debe tener almenos un numero, una mayuscula, una minuscula y no tener un espacio')
