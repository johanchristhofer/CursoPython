#Concatenando ó sumando string
a = 'Hola'
b = 'Mundo'
frase = a + b
#frase = a+b = HolaMundo
print(frase)

#Imprimiendo un caracter de una cadena
print(frase[2])
#frase = HolaMundo

#Imprimiendo un fragmento
print(frase[1:5])
#frase = HolaMundo

#Imprimiendo inicio y final
print(frase[:5])
print(frase[2:])
#frase = HolaMundo

#Posiciones negativas
print(frase[-4:-2])
#frase = HolaMundo

#La cantidad de caracteres de un string
print(len(frase))