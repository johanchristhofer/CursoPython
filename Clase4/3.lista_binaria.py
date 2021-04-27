def binaria_busqueda(lista,numero_busqueda,low,high):
    
    if low > high:
        return False
    mid=(low+high)//2

    if lista[mid]==numero_busqueda:
        return True
    elif lista[mid]>numero_busqueda:
        return binaria_busqueda(lista,numero_busqueda,low,mid-1)
    else:
        return binaria_busqueda(lista,numero_busqueda,mid+1,high)


if __name__=='__main__':
    #Lista ordenada de menor a mayor
    lista=[1,3,4,5,6,7,8,10,25,27,28,34,49,51]
    numero_busqueda=int(input("Ingrese el número: "))
    respuesta=binaria_busqueda(lista,numero_busqueda,0,len(lista)-1)
    
    if respuesta==True:
        print("El número es el buscado")
    else:
        print("El número no es el buscado")