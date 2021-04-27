frutas = ["plátano", "pera", "manzana", "naranja"]

#busqueda por index
print(frutas[2])
print(frutas[-2])
print(frutas[0:3])

#cantidad elementos
x=len(frutas)
print(x)

#incrustar un dato a lista ( coloca al final)
frutas.append("fresa")
print(frutas)

#incrustar en una posición especifica
frutas.insert(2,"uva")
print(frutas)

#busqueda de elementos
x=frutas.index("naranja")
print(x)

#borrar un elemento acorde al valor
frutas.remove("uva")
print(frutas)

#borrar un elemento acorde a su posición
frutas.pop(4)
print(frutas)

#Copiar una lista en otra
mylista=frutas.copy()
print(mylista)

numeros = [ 31, 3, 11, 9, 24, 5]
print(numeros)
numeros.sort() #Ordena  la lista ascendente
print(numeros)
numeros.reverse() #Ordena  la lista descendente
print(numeros)
frutas.sort()
print(frutas)

#borrar limpiar todo
frutas.clear()
print(frutas)


