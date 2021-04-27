# -*- coding: utf-8 -*-
""" Ex 1
 Diseña una función que, dada una lista de listas, que representa una matriz
   de nf filas y nc columnas,devuelva una lista con el calculo del mayor valor
   de cada columna
"""
def max_columnas(lst):
    """ calcula lista con el valor máximo de cada columna
    >>> max_columnas([[2,3,4],[3,5,3],[1,1,2]])
    [3, 5, 4]
    """
    nf = len(lst)
    nc = len(lst[0])
    Mayor = lst[0]
    for i in range(1,nf):
        for j in range(nc):
            if lst[i][j]>Mayor[j]:
                Mayor[j] = lst[i][j]
    return Mayor
# opción inicializando los valores en -infinito
def max_columnas2(lst):
    """ calcula lista con el valor medio de cada columna
    >>> max_columnas2([[2,3,4],[3,5,3],[1,1,2]])
    [3, 5, 4]
    """
    nf = len(lst)
    nc = len(lst[0])
    res = nc*[float('-inf')]
    for i in range(nf):
        for j in range(nc):
            if lst[i][j]>res[j]:
                res[j] = lst[i][j]
    return res
""" Ex 2
Diseña una función que, dada una lista de listas, que representa una matriz
   (los elementos de la lista son las filas de la matriz), de nf filas y 
   nc columnas, devuelva una lista con el cálculo del valor medio de cada fila.
   Ejemplo:
    >>> M = [[1,2,3,4],[1,3,5,7]]
    >>> media_filas(M)
    [3.5,4.0]
"""

def media_filas(lst):
    """calculo lista con el valor medio de cada fila
    >>> media_filas([[1,2,3,4],[1,3,5,7]])
    [2.5, 4.0]
    """
    nf = len(lst)
    nc = len(lst[0])
    res = []
    for i in range(nf):
         s = sum(lst[i])
         res.append(s/nc)
    return res

""" Ex 3
 Diseña una función que, dada una lista de listas, que representa una matriz
   de nf filas y nc columnas,devuelva una lista con el calculo del valor medio 
   de cada columna.Ejemplo:
    >>> M2 = [[2,3,4],[3,3,3]]
    >>> media_columnas(M2)
    [2.5,3.0,3.5]
    
"""
def media_columnas(lst):
    """ calcula lista con el valor medio de cada columna
    >>> media_columnas([[2,3,4],[3,3,3]])
    [2.5, 3.0, 3.5]
    """
    nf = len(lst)
    nc = len(lst[0])
    res = nc*[0]
    for i in range(nf):
        for j in range(nc):
            res[j] += lst[i][j]/nf
    return res
""" Ex 4
 Función que devuelva cuál es la fila con su mayor suma de elementos y su suma
 """
def mayor_fila(m):
    """ 
    >>> mayor_fila([[1,2,3],[3,3,3],[1,3,2]])
    (1, 9)
    """
    nf = len(m)
    Mayor = sum(m[0])
    pos = 0
    for i in range(1,nf):
        suma = sum(m[i])
        if suma>Mayor:
            Mayor=suma
            pos=i
    return pos, Mayor
""" Ex 5
Función que devuelve True si una matriz es diagonal
"""
def es_diagonal(m):    # con for, búsqueda en Python
    N = len(m)
    for i in range(N):
        for j in range(N):
            if i != j and m[i][j] != 0:
                return False
    return True
def es_diagonalW(m):    # con while, búsqueda en Python
    N = len(m)
    i=0
    while i<N:
        j = 0
        while j<N:
            if i != j and m[i][j] != 0:
                return False
            j += 1
        i +=1
    return True
    return True
def es_diagonalWG(m):    # con while, búsqueda General otros lenguajes
    N = len(m)
    OK = True
    i=0
    while i<N and OK:
        j = 0
        while j<N and OK:
            if i != j and m[i][j] != 0:
                OK = False
            j += 1
        i +=1
    return OK
""" Ex 6
Función que devuelve True si una matriz es identidad
"""
def es_identidad(m):    # con for, búsqueda en Python
    N = len(m)
    for i in range(N):
        for j in range(N):
            if i != j and m[i][j] != 0 or i==j and m[i][j]!=1:
                return False
    return True

# Listas de listas heterogéneas
# Ex 1 Gestionar Pensionistas 
lst = [['1111A','Carlos',68,640,589,573],
     ['2222D','Lucia',69,710,550,570,698,645,512],
     ['3333J','Paula',72,530,534],
     ['4444N','Luis',75,770,645,630,650,590,481,602]]
# a) mediaGastos(p)  dada una lista conlos datos de un pensionista p, 
#   devuelva el promedio de los gastos con dos cifras decimales
def mediaGastos(p):
    """
    >>> mediaGastos(lst[0])
    600.67
    """
    s = sum(p[3:])
    n = len(p[3:]) 
    return round(s/n,2)
# b) mediaEdad(lst) 
def mediaEdad(lst):
    """
    >>> mediaEdad(lst)
    71.0
    """
    n = len(lst)
    s = 0
    for p in lst:
        s += p[2]
    return round(s/n,1)
# c) EdadesExtremas(lst) 
def EdadesExtremas(lst) :
    """
    >>> EdadesExtremas(lst) 
    (68, 75)
    """
    M = lst[0][2]
    m = lst[0][2]
    for p in lst[1:]:
        if p[2] > M:
            M = p[2]
        if p[2] < m:
            m = p[2]
    return m, M
def EdadesExtremas1(lst) :
    """
    >>> EdadesExtremas1(lst) 
    (68, 75)
    """
    M = -1
    m = float('inf')
    for p in lst:
        if p[2] > M:
            M = p[2]
        if p[2] < m:
            m = p[2]
    return m, M
def EdadesExtremas2(lst):  # formando lista de edades
    """
    >>> EdadesExtremas2(lst) 
    (68, 75)
    """
    edad = []
    for i in lst:
        edad.append(i[2])
    return min(edad), max(edad)
# d) sumapromedios
def sumaPromedio(lst):
    """
    >>> sumaPromedio(lst)
    2370.84
    """
    s = 0
    for p in lst:
        s += mediaGastos(p)
    return s

# e) MediaMaxima(lst) 
def MediaMaxima(lst):
    """
    >>> MediaMaxima(lst)
    624.0
    """
    MedMayor = mediaGastos(lst[0])
    for p in lst[1:]:
        m = mediaGastos(p)
        if m > MedMayor:
            MedMayor = m
    return MedMayor
def MediaMaxima2(lst):    # opción creando una lista y buscando el mayor valor
    """
    >>> MediaMaxima2(lst)
    624.0
    """
    lstaux=[]
    for p in lst:
        lstaux.append(mediaGastos(p))
    return round(max(lstaux),2)
# f) GastoPromedio(lst) 
def GastoPromedio(lst):
    """
    >>> GastoPromedio(lst)
    [532.0, 600.67, 614.17, 624.0]
    """
    lstR = []
    for p in lst:
        lstR.append(mediaGastos(p))
    lstR.sort()
    return lstR
# g) Primera persona de la lista con gasto promedio superior a d
# Busqueda en Python con for
def gastoPromedioSuperior(lst, d):
    """
    >>> gastoPromedioSuperior(lst, 600)
    ['1111A', 68]
    """
    for p in lst:
        if mediaGastos(p) > d:
            return [p[0], p[2]]
    return []

# Ex 2


def edad_m_pacientes(lst):
    """
    >>> paciente1 = ['Puig','c1234', 56]
    >>> lst2 = [paciente1,['Marti','c3456',39],['Smith','c543',45]]
    >>> edad_m_pacientes(lst2)
    46.7
    """
    N = len(lst)
    suma = 0
    for i in range(N):
        suma += lst[i][2]
    return round(suma/N,1)

""" Ex 3 Clientes VIP, devolver nombres de clientes que hayan gastado mas de
1000 euros y tengasn al menos 3 compras.
"""
def vip(lst):
    """
    >>> vip([['pepe', 350, 505, 200], ['juan', 590, 650], \
             ['paula', 100, 105, 450], ['ana', 650, 351, 5]])
    ['ana', 'pepe']
    >>> vip([['juan', 590, 650], ['paula', 100, 105, 450, 95], \
             ['sara', 350, 350, 300]])
    []
    >>> vip([['89GR', 348, 943, 304], ['09PY', 932, 894, 49, 49], \
             ['64FF', 8932, 3290, 320]])
    ['09PY', '64FF', '89GR']
    """
    res = []
    for cliente in lst:
        if sum(cliente[1:])>1000 and len(cliente[1:])>2:
            res.append(cliente[0])
    res.sort()       
    return res

""" Ex 4. Mejor herramienta. Se usarará la función std(lst) previamente
          diseñada para hallar la desviación estándar
"""
def std(v):
    if len(v) == 0:
        return 0
    m = sum(v)/len(v)
    v = v[:]
    for i in range(len(v)):
        v[i] = (v[i] - m)**2
    num = sum(v)
    return (num/(len(v)-1))**0.5

def mejor_herramienta(lst):
    """
    >>> m = [['herramienta1',1.29708186, 1.31266035, 1.33536083, 1.29651107, \
                        1.27489226, 1.31669962, 1.296645  , 1.31999788,  \
                        1.30039536, 1.28287777, 1.28805435, 1.30090147,  \
                        1.27151722, 1.26324628, 1.2893031 , 1.30099176,  \
                        1.29308506, 1.30773716, 1.29497462, 1.29530172],  \
            ['herramienta2',2.82486964, 2.79124532, 2.80591011, 2.80944679, \
                        2.81057422, 2.7981161 , 2.77104033, 2.79758669,  \
                        2.78554721, 2.80345295, 2.79900319, 2.7846449 ,  \
                        2.80583578, 2.81153274, 2.80816726, 2.81009209,  \
                        2.7946134 , 2.7883018 , 2.7968774 , 2.78145684],  \
            ['herramienta3',1.59912295, 1.60199575, 1.59920467, 1.60108844, \
                        1.60497468, 1.59742797, 1.6009022 , 1.59948543,  \
                        1.60242975, 1.60092409, 1.59868339, 1.59909426,  \
                        1.59670533, 1.59309514, 1.60266672, 1.59587891,  \
                        1.59662104, 1.60692734, 1.60238514, 1.60106771], \
            ['herramienta4',0.91837844, 0.91031125, 0.87873479, 0.91919775, \
                        0.94548981, 0.92281759, 0.87520564, 0.90950628,  \
                        0.91250966, 0.90622502, 0.90045178, 0.89656651,  \
                        0.92379851, 0.90519854, 0.87822092, 0.83423747,  \
                        0.92680545, 0.9184275 , 0.9108524 , 0.88113948], \
            ['herramienta5',1.89940911, 1.90002205, 1.89982581, 1.90027163, \
                        1.89981981, 1.89991447, 1.89988227, 1.90011783,  \
                        1.90013265, 1.89962221, 1.90012783, 1.89985387,  \
                        1.90009801, 1.89989183, 1.89987518, 1.8993762 ,  \
                        1.89976188, 1.89942767, 1.89992038, 1.89967331],  \
            ['herramienta6',2.02130853, 1.99060463, 2.01337742, 1.99429791, \
                        1.98339322, 1.99800895, 2.0008932 , 2.0228473 ,  \
                        2.00771829, 2.00002554, 1.99437905, 2.01117355,  \
                        1.99537268, 2.00808408, 1.99111077, 1.98352936,  \
                        1.99376165, 1.98541568, 2.00602666, 2.00810295]]
    >>> mejor_herramienta(m)
    'herramienta5'
    """
    menor = ''
    M = float('inf')
    for h in lst:
        s = std(h[1:])
        if s < M:
            M = s
            menor = h[0]
    return menor

if __name__=="__main__":
    import doctest
    print(doctest.testmod())

    