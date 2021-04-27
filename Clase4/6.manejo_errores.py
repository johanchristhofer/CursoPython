# -*- coding: utf-8   Para acentos, letra eñe -*-
countries={
    'peru': 31,
    'colombia': 49,
    'argentina': 43,
    'mexico': 122,
    'chile': 18

}

while True:
    contry = input("Ingrese el nombre del país: ").lower()
    
    try:
        print(f"La población de {contry} es: {countries[contry]} millones ")

    except KeyError:
        print(f"No tenemos registrado el dato del pais: {contry}")