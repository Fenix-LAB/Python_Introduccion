############## Podemos usar todas las operaciones matemáticas #######################
# + (suma)
# * (multiplicación)
# - (resta)
# / (división)
# // (división entero)
# % (módulo)
# ** (elevar a una potencia)

################################### Variables ####################################

# int
# float
# bool
# str
# bytes
#b = b"0x101"

# Reasignacion de variables

# Funcion type(), devuelve el tipo de dato de la variable

# Multiple asignacion

# Conversion

############################## Metodos de Strings ##############################

# txt.upper()
# txt.lower()
# txt.capitalize()
# txt.replace()
# txt.split()
# txt.join()

################################# Listas #####################################

# Lista homogenea

# Lsta no homogenea

# Indexar

#lista = [3, 6, 2, 8, 1, 9, 4]

# Agregar un elemento al final de la lista
#lista.append(7)

# Agregar varios elementos al final de la lista
#lista.extend([10, 11, 12])

# Agregar un elemento en una posición específica de la lista
#lista.insert(2, 5)

# Eliminar el primer elemento de la lista que coincide con un valor específico
#lista.remove(9)

# Eliminar y devolver el elemento en una posición específica de la lista
#elemento = lista.pop(4)

# Obtener la posición del primer elemento específico en la lista
#posicion = lista.index(8)

# Obtener el número de veces que un elemento específico aparece en la lista
#conteo = lista.count(5)

# Ordenar la lista en orden ascendente
#lista.sort()

# Invertir el orden de los elementos en la lista
#lista.reverse()

# Lista con Lista [1,2,3,[4,5,'cadena',['nueva cadena']]]

############################ Diccionarios  ###################################

"""datos = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "profesión": "Ingeniero"
}"""

# Indexar en diccionarios

#diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
# print(diccionario['nombre'])

# Obtener una lista con todas las claves del diccionario
#claves = diccionario.keys()

# Obtener una lista con todos los valores del diccionario
#valores = diccionario.values()

# Obtener el valor asociado a una clave específica
#edad = diccionario.get('edad')

# Eliminar una clave y su correspondiente valor del diccionario
#del diccionario['ciudad']

# Eliminar todos los elementos del diccionario
#diccionario.clear()

########################### Tuplas ####################################

# Es un tipo de dato inmutable con elementos entre paréntesis separados por comas
#t1 = (1,2,3)

####################### Operadores logicos y condicional if ###############################

# Ejemplo de operadores lógicos en Python
"""x = 12
y = 10
z = 15"""

# Operador and
"""if x < y and y < z:
    print("x es menor que y y y es mayor que z")"""

# Operador or
"""if x > y or y > z:
    print("x es mayor que y o y es mayor que z")"""

# Operador not
"""if not(x == y):
    print("x no es igual a y")"""

# El condicional 'if' (si)
"""x=2
if x<3:
    print('Es menor')"""

# Else
"""x=4
if x<3:
    print('Es menor')
else:
    print('Es mayor')"""

#Elif
"""x=3
if x<3:
    print('Es menor')
elif x==3:
    print('Es igual')
else:
    print('Es mayor')"""

############################# Bucle for #################################


############################# Bucle while #################################


############################# Funciones #####################################


############################# Funciones Lambda ################################

# fl = lambda var:var**2
# x = lambda a, b, c : a + b + c