# -*- coding: utf-8 -*-
"""
Ejercicios 2.1 strings
"""

"""Strings
Recorrido
Ej 1. 
"""
def maximo(s):
    """
    >>> maximo('')
    False
    >>> maximo('abaco')
    'o'
    >>> maximo('india')
    'n'
    >>> maximo('Urales')
    's'
    """
    if len(s) == 0:
        return False
    else:
        mayor = s[0]
        for n in s:  # mejor: for n in s[1:]
            if mayor < n:
                mayor = n
        return mayor

def maximo2(s):
    if len(s) == 0:
        return False
    else:
        return max(s)

# Ej. 2
def contarLetra(st,letra):
    """Contar letra en el string str
    >>> contarLetra('patata caliente','a')
    4
    >>> contarLetra('Esplugues','a')
    0
    """
    n = 0
    for car in st:
        if car == letra:
            n = n + 1
    return n
# opción con método .count()
def contarLetra2(st,letra):
    """Contar letra en el string str
    >>> contarLetra2('patata caliente','a')
    4
    >>> contarLetra2('Esplugues','a')
    0
    """
    return st.count(letra)
""" Replace
 Ej 3. 
"""
def cambia(s,c1,c2):
    """Cambia caracter c1 por c2 (si existe c1)
    Hay que crear otro string!
    Ejemplos:
    >>> cambia('patata','a','e')
    'petete'
    >>> cambia('camion','o','ó')
    'camión'
    >>> cambia('patata','e','i')
    'patata'
    """
    #n = len(s)
    sc = ''  # string cambiado
    for c in s:
        if c == c1:
            sc = sc + c2
        else:
            sc = sc + c
    return sc
if __name__ == "__main__":
    print(cambia('Barcelona','a','e'))
    print(cambia('barco','o','a'))
    import doctest
    doctest.testmod(verbose=True)

""" OPción con método s.replace()
"""
def cambia2(s,c1,c2):
    """Cambia caracter c1 por c2 (si existe c1)
    Hay que crear otro string!
    Ejemplos:
    >>> cambia2('patata','a','e')
    'petete'
    >>> cambia2('camion','o','ó')
    'camión'
    >>> cambia2('patata','e','i')
    'patata'
    """
    return s.replace(c1,c2)
""" Con índices, general para otros lenguajes
"""
def cambia3(s,c1,c2):
    """Cambia c1 por c2 en string s (si existe c1)
    Hay que crear otro string!
    >>> cambia3('casado','a','e')
    'cesedo'
    """
    n = len(s)
    sc = ''
    for i in range(n):
        if s[i] == c1:
            sc = sc + c2
        else:
            sc = sc + s[i]
    return sc

""" Búsqueda
 Ej. 4. Buscar k-aésima posición de 'a'
"""
def pos_a(s, k):
    """
    >>> pos_a('', 1)
    -1
    >>> pos_a('hola', 2)
    -1
    >>> pos_a('ara', 3)
    -1
    >>> pos_a('lalaland', 3)
    5
    >>> pos_a('almendro', 1)
    0
    """
    pos = 0
    na = 0
    for c in s:
        if c == 'a':
            na += 1
            if na == k:
                return pos
        pos += 1
    return -1

# Ej 5
def cambia_minMay(s):
    """ Cambia vocales minúsculas a mayúsculas
    >>> cambia_minMay('Casablanca 20 Madrid 30')
    'CAsAblAncA 20 MAdrId 30'
    >>> cambia_minMay('Valencia - Alicante en 2 horas')
    'VAlEncIA - AlIcAntE En 2 hOrAs
    """
    s1 = ''
    for x in s:
        if x.islower() and x in 'aeiou':
            s1 += x.upper()
        else:
            s1 += x
    return s1
#Ej 6
def delNumbers(s):
    """ Borra los números de un string
    >>> delNumbers('Alicante a 20 kms')
    'Alicante a  kms'
    >>> delNumbers('Casa_1234, Bcn25')
    'Casa_, Bcn'
    """
    s1 = ''
    for x in s:
        if not x.isdecimal():  # if not x in [0123456789]
            s1 += x
    return s1
# Ej 7
def contarMm(s):
    """ Devuelve la tupla del número de mayúsculas y munúsculas de str
    >>> contarMm('Hola')
    (1, 3)
    >>> contarMm('Ella dijo: HOLA')
    (5, 7)
    """
    M = 0
    m = 0
    for letra in s:
        if letra.isupper():
            M += 1
        if letra.islower():
            m += 1
    return M,m
# Ej 8
def contar_vocal_cons(s):
    """ Cuenta el núemro de vocales y consonantes de s
    >>> contar_vocal_cons('Aprendo Python')
    (4, 9)
    """
    v = 0
    c = 0
    vocal = 'aeiouAEIOU'
    cons = 'bcdfghjklmnpqrstvwxyz'
    cons = cons+cons.upper()
    for letra in s:
        if letra in vocal:
            v += 1
        #if letra in cons:
        if letra.isalpha() and letra not in vocal:
            c += 1
    return v,c

# E9 9
clave = 'ixmrklstnuzbowfaqejdcpvhyg'
def encripta(s,clave):
    """ Encripta el string s con el diccionario dado por la clave
    >>> encripta('cafe', 'ixmrklstnuzbowfaqejdcpvhyg')
    'milk'
    >>> encripta('dame 1 chocolate', 'ixmrklstnuzbowfaqejdcpvhyg')
    'riok 1 mtfmfbidk'
    """
    a='abcdefghijklmnopqrstuvwxyz'
    s1 = ''
    for c in s:
        if c in a:
            i = a.find(c)
            s1 += clave[i]
        else:
            s1 += c
    return s1
#Ej 10
def desencripta(s,clave):
    """ Desencripta s que tiene la clave 'clave'
    >>> clave = 'ixmrklstnuzbowfaqejdcpvhyg' 
    >>> desencripta('milk',clave)
    'cafe'
    >>> desencripta('riok 1 mtfmfbidk',clave)
    'dame 1 chocolate'

    """
    a='abcdefghijklmnopqrstuvwxyz'
    s1 = ''
    for c in s:
        if c in clave:
            i = clave.find(c)
            s1 += a[i]
        else:
            s1 += c
    return s1

# Ej 11
def reagrupar(s):
    """ Reagrupa letras minúsculas y a continuación digitos decimales
        del string dado. Ejemplo
    >>> reagrupar('r2b2')
    'rb22'
    >>> reagrupar('a45tr09pw')
    'atrpw4509'
    >>> reagrupar('nonumbers')
    'nonumbers'
    >>> reagrupar('543210')
    '543210'
    """
    s_reag = ''  # string vacio, empty string
    for c in s:
        if 'a' <= c <= 'z': #equivale a if c.islower():
            s_reag += c     # s = s + c
    for c in s:
        if c in '0123456789':  #equivale a if c.isdecimal()
            s_reag += c   # s = s + c
    return s_reag

# Opción con un solo for
def regroup(s):
    """ Reagrupa letras minúsculas y a continuación digitos decimales
        del string dado. Ejemplo
    >>> regroup('r2b2')
    'rb22'
    >>> regroup('a45tr09pw')
    'atrpw4509'
    >>> regroup('nonumbers')
    'nonumbers'
    >>> regroup('543210')
    '543210'
    """
    slet = ''
    snum = ''
    for c in s:
        if 'a' <= c <= 'z':     # if c.islower():
            slet = slet + c        # slet = slet + c
        elif c in '0123456789':   # if c.isdecimal()
            snum += c
    return slet + snum

# Ej 12
def t_descubierto(s):
    """Evolución cola. +: entra, -: sale persona a/de la cola por segundo.
    Está lloviendo y solo las tres primeras personas de la cola pueden ponerse
    a cubierto.
    La función retorna durante cuantos segundos ha habido gente
    en la cola mojandose, si solo las 3 primeras
    pueden estar a cubierto.
    >>> t_descubierto('++++--+')
    1
    >>> t_descubierto('++++++++++----+')
    12
    >>> t_descubierto('+-++--+++---++--')
    0
    """
    cola_len = 0
    seg_moj = 0
    for c in s:
        if c == '+':
            cola_len += 1
        else:
            cola_len -= 1
        if cola_len > 3:
            seg_moj += 1
    return seg_moj

""" 13. Vuelve Robot
""" 
def vuelve(s):
    """ un robot que se desplaza dando pasos de 60 centímetros siguiendo 
    cuatro direcciones norte, sur, este y oeste  
    Dado un string orden formado con las letras n, s, e y o,
    retorna True si y solo si el robot termina en la posición de salida.
    >>> vuelve('nseo')
    True
    >>> vuelve('nen')
    False
    """
    x, y = 0, 0
    for c in s:
        if c == 'n':
            y += 60
        elif c == 's':
            y -= 60
        elif c == 'e':
            x += 60
        elif c == 'o':
            x -= 60
       
    return x == 0 and y == 0

""" 14. Cuenta atomos
"""
def cuenta_atomos(s):
    """
    >>> cuenta_atomos('HIO')
    3
    >>> cuenta_atomos('H2O')
    3
    >>> cuenta_atomos('C2H5O')
    8
    >>> cuenta_atomos('CaCO3')
    5
    >>> cuenta_atomos('Fe3O4')
    7
    """
    dec = '23456789'
    num = 0
    for c in s:
        if c.isupper():
            num = num + 1
        elif c in dec:
            num = num + int(c)-1
    return num


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
