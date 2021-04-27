def is_prime(numero):
    if numero <2:
        return False
    elif numero==2:
        return True
    elif numero>2 and numero % 2==0:
        return False
    else:
        for i in range(3, numero):
            if numero%i==0:
                return False
    return True

def run():
    numero=int(input('Ingresa el número: '))
    resultado=is_prime(numero)
    
    if resultado==True:
        print("El numero es primo")
    else:
        print("El número no es primo")     

if __name__=='__main__': #Se ejecuta run
    run()