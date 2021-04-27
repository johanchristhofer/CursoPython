thisdict = {"marca":"Ford","modelo": "Mustang","año": 1964}
#impriendo diccionario
print(thisdict)

#imprimiendo los keys(llaves)
x = thisdict.keys()
print(x)

#imprimir el valor de una llave
num=thisdict.get("año")
print(num)

#imprimir los valores de las llaves
x = thisdict.values()
print(x)

#cambiar un valor 
thisdict["marca"]="Audi"
print(thisdict)

#obtener elementos de un diccionario
y=thisdict.items()
print(y)

#eliminando un elemento
thisdict.pop("marca")
print(thisdict)

#eliminando un elemento final
thisdict.popitem()
print(thisdict)

#limpiando todo
thisdict.clear()
print(thisdict)



