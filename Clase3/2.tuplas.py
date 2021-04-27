tupla = ("manzana","platano","fresa")
print(type(tupla))

#tamaño de una tupla
print(len(tupla))

#elemento de una tupla
print(tupla[1])

#convirtiendo una tupla en lista
y=list(tupla)
y[1]="naranja" #reemplazar un elemento de la lista
print(y)
#convirtiendo una lista en tupla
tupla=tuple(y)
print(type(tupla))
print(tupla)
