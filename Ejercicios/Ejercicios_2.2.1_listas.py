# -*- coding: utf-8 -*-
# Ej 1
def comienza_letra(s,letra):
    """Cuenta palabras que comienzan por letra (minúscula o mayúscula)
    >>> comienza_letra('Este día comenzamos a estudiar algoritmos', 'e')
    2
    """
    l = s.split()
    cont = 0
    for p in l:
        if p[0] == letra.upper() or p[0] ==letra.lower():
            cont += 1
    return cont
# Ex 2
def palabra_mas_larga(s):
    """devuelva la palabra de mayor longitud (la primera encontrada si hay 
    más de una del mismo tamaño)
    >>> palabra_mas_larga('Ayer comenzamos a estudiar algoritmos')
    'comenzamos'
    """
    lst = s.split()
    pml = lst[0]
    LongMax = len(lst[0])
    for p in lst:
        if len(p) > LongMax:
            pml = p
            LongMax = len(p)
    return pml
# Ex 3 ConvertirFecha
def convfecha(fecha):
    """
    >>> convfecha('12/07/2017')
    [12, 7, 2017]
    """
    lst = fecha.split('/')
    for i in range(3):
        lst[i] = int(lst[i])
    return lst
# Ex 4. Busca si hay al menos dos strings en lst que empiecen por mayúscula,
#       o False si no los hay
def  Mayus(str):
    return str[0].isupper()
def BuscaTexto(lst):
    """
    >>> BuscaTexto(['hola', 'silla', 'mesa'])
    False
    >>> BuscaTexto(['cuadrado rojo', 'Coche', 'bosque'])
    False
    >>> BuscaTexto(['boĺıgrafo', 'Aventura', 'bici', 'Casco', 'Horno'])
    True
    >>> BuscaTexto([])
    False
    >>> BuscaTexto(['plane'])
    False
    >>> BuscaTexto(['Jet'])
    False
    >>> BuscaTexto(['plane', 'Jet', 'rocket', 'UFO'])
    True
    >>> BuscaTexto(['plane', 'jet', 'rocket', 'UFO'])
    False
    """
    c = 0
    for w in lst:
        if Mayus(w):
            c += 1
        if c == 2:
            return True
    return False

# Ex 5
def listaMultiplos(lst,m):
    """ Devuelve lista con los múltiplos de m en lst
    >>> listamultiplos([1,2,3,4,5,6,7,8,9,10,11,12],3)
    [3, 6, 9, 12]
    >>> listaMultiplos([1,2,3,4,5,6,7,8,9,10,11,12],5)
    [5, 10]
    """
    lm = []
    for x in lst:
        if x % m == 0:
            lm.append(x)
    return lm
# Ex 6
def PositNegat(lst):
    """devuelve 2 listas, una con los Valores positivos o 0 y otra con los 
    negativos
    >>> PositNegat([69, -37, 0,  -27, -59, 83, 1, 45])
    ([69, 0, 83, 1, 45], [-37, -27, -59])
    """
    pos, neg = [], []
    for n in lst:
        if n >= 0:
            pos.append(n)
        else:
            neg.append(n)
    return pos, neg
# variación donde se devuelven las listas ordenadas
def PositNegatOrd(lst):
    """
    >>> PositNegatOrd([69, -37, 0,  -27, -59, 83, 1, 45])
    ([0, 1, 45, 69, 83], [-59, -37, -27])
    """
    pos, neg = [], []
    for n in lst:
        if n >= 0:
            pos.append(n)
        else:
            neg.append(n)
    pos.sort()
    neg.sort()
    return pos, neg

# Ex 7 
def parImpar(lst):
    """
    >>> parImpar([1,2,3,4,5,6,7,8])
    ([2, 4, 6, 8], [1, 3, 5, 7])
    >>> parimpar([1,3,5])
    ([], [1, 3, 5])
    """
    par = []
    impar = []
    for v in lst:
        if v % 2 == 0:
            par.append(v)
        else:
            impar.append(v)
    return par,impar
def parImpar2(lst):
    """ Concatenar en lugar de append
    >>> parImpar([1,2,3,4,5,6,7,8])
    ([2, 4, 6, 8], [1, 3, 5, 7])
    >>> parimpar([1,3,5])
    ([], [1, 3, 5])
    """
    par = []
    impar = []
    for v in lst:
        if v % 2 == 0:
            par += [v]
        else:
            impar += [v]
    return par,impar
# Ex 8 EliminarRepetidos
def eliminarRepet(lst):
    """
    >>> eliminarRepet([1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    f = [lst[0]]
    for i in lst:
        if i not in f:
            f.append(i)
    return f
    # Otra opción
def eliminarRepet2(lst):
    """
    >>> eliminarRepet([1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> eliminarRepet([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    """
    res = []
    for i in range(len(lst)):
        if lst[i] not in lst[i+1:]:    
            res.append(lst[i])          # res += [lst[i]]
    return res
# Ex 9
def mueve_derecha(lst):
    """
    >>> lst=[2, 4, 6, 8, 10]
    >>> mueve_derecha(lst)
    >>> print(lst)
    [10, 2, 4, 6, 8]
    """
    last = lst[-1]
    for i in range(len(lst)-1, 0, -1):
        lst[i] = lst[i-1]
    lst[0] = last
# Ex 10
def mueve_izquierda(lst):
    """
    >>> lst=[2, 4, 6, 8, 10]
    >>> mueve_izquierda(lst)
    >>> lst
    [4, 6, 8, 10, 2]
    """
    first = lst[0]
    lst.remove(first)
    lst.append(first)
"""11 a) Se pide diseñar una función que, dada una lista de temperaturas medidas 
cada hora a un niño, calcular el número de incrementos de temperatura 
(en una hora respecto a la hora anterior) de al menos 1 ºC de temperatura 
cuando se tenia fiebre (temperatura >= 38ºC). 
La función debe devolver el números incrementos de al menos 1 ºC encontrados 
cuando la temeperatura sea de al menos 38ºC. Si no hay estos incrementos
devolverá 0.
"""
def incrTempN(lst):
    """
    >>> incrTempN([36,37,37.2,36.8,38,37.5,37.6,38.1,37,37.3])
    0
    >>> incrTempN([36,37,37.2,36.8,38,38.2,39.2,38.1,37,37.3])
    1
    """
    i = 1
    inc_ge = 0
    while i < len(lst):
        if lst[i]-lst[i-1] >=1 and lst[i-1] >= 38:
            inc_ge += 1
        i += 1
    return inc_ge

""" b) Se pide diseñar una función que, dada una lista de temperaturas medidas
cada hora a un niño, calcular los incrementos de temperatura (en una hora
respecto a la hora anterior) de al menos 1 ºC de temperatura cuando se 
tenia fiebre (temperatura >= 38ºC) y devolver estos incrementos en una lista. 
La función debe devolver una lista con los valores de los incrementos 
de al menos 1 ºC cuando la temeperatura sea de al menos 38ºC. 
Si no hay incrementos (para valores >= 30ºC) se devolverá la lista vacía. 
"""
def incrTempL(lst):
    """
    >>> incrTempL([36,37,37.2,36.8,38,37.5,37.6,38.1,37,37.3])
    []
    >>> incrTempL([36,37,37.2,36.8,38,39.5,38.7,39.7,37,37.3])
    [1.5, 1.0]
    """
    i = 1
    inc_ge = []
    while i < len(lst):
        if lst[i]-lst[i-1] >=1 and lst[i-1] >= 38:
            inc_ge.append(lst[i]-lst[i-1])
        i += 1
    return inc_ge

""" c) Se pide diseñar una función que, dada una lista de temperaturas medidas
cada hora a un niño, buscar si hay en alguna hora un incremento (respecto a la 
hora anterior) de al menos 1 ºC de temperatura cuando se tenia fiebre 
(temperatura >= 38ºC). 
La función debe devolver el valor del primer incremento de al menos 1 ºC
encontrado y la hora que ocurrió. 
Si no hubiera incrementos de 1ºC cuando hay fiebre, la función devuelve -1 
tanto para el incremento como para la hora.
"""
#Solución estructurada
def incrTempB(lst):
    """
    incrTempB([36,37,37.2,36.8,38,37.5,37.6,38.1,37,37.3])
    (-1, -1)
    >>> incrTempB([36,37,37.2,36.8,38,38.2,39.2,38.1,37,37.3])
    (1.0, 6)
    """
    i = 1
    Trobat = False
    inc_ge = -1
    pos = -1
    while i < len(lst) and not Trobat:
        if lst[i]-lst[i-1] >=1 and lst[i-1] >= 38:
            inc_ge = lst[i]-lst[i-1]
            pos = i
            Trobat = True
        i += 1
    return inc_ge, pos


# Solución opción más de Python
def incrTempB2(lst):
    """
    incrTempB2([36,37,37.2,36.8,38,37.5,37.6,38.1,37,37.3])
    (-1, -1)
    >>> incrTempB2([36,37,37.2,36.8,38,38.2,39.2,38.1,37,37.3])
    (1.0, 6)
    """
    i = 1
    while i < len(lst):
        if lst[i]-lst[i-1]>=1 and lst[i-1] >= 38:
            inc_ge = lst[i]-lst[i-1]
            pos = i
            return inc_ge, pos
        i += 1
    return -1, -1


