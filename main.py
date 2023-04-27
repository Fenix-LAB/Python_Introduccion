############## Podemos usar todas las operaciones matemáticas #######################
# + (suma)
# * (multiplicación)
# - (resta)
# / (división)
# // (división entero)
# % (módulo)
# ** (elevar a una potencia)

# int nameVar = 5
nameVar = 5
varNueva = 10

res = nameVar ** varNueva

################################### Variables ####################################

# int
varInt = 5
# float
varFloat = 0.5
# bool
varBool = False
# str
varString = 'Hola'
# bytes
b = b"0x101"



# Reasignacion de variables
varInt = "Hola a todos"

# Funcion type(), devuelve el tipo de dato de la variable
# print(type(varInt))


# Multiple asignacion
a, c, d= 5, "Hola", 7.0
# print(a, c, d)

# Conversion
new = str(varFloat)

str_1 = '150'
newV_Int = int(str_1)
#print("Tipo: ", type(newV_Int),"Valor ", newV_Int)

# type(nombre_de_la_variable)

############################## Metodos de Strings ##############################
txt = 'hola a todos, espero que no tengan dudas'
#lis = ['hola', 'a', 'todos']

# x = txt.upper()
# x = txt.lower()
# x = txt.capitalize()
# x =  txt.replace("hola", "adios")
# x = txt.split()
# x =  lis.join()


# print(x)

################################# Listas #####################################

# Lista homogenea
lis = [1, 2, 3, 4]

# Lsta no homogenea
lis2=[1, 'hola',7.0]

lista = [3, 6, 2, 8, 1, 9, 4, 3]
#print(lista)
# Agregar un elemento al final de la lista
# lista.append(7)

# Agregar varios elementos al final de la lista
# lista.extend([10, 11, 12])

# Agregar un elemento en una posición específica de la lista
# lista.insert(2, 5)
# .inster(pos, val)

# Eliminar el primer elemento de la lista que coincide con un valor específico
# lista.remove(9)

# Eliminar y devolver el elemento en una posición específica de la lista
# elemento = lista.pop(4)

# Obtener la posición del primer elemento específico en la lista
# posicion = lista.index(8)

# Obtener el número de veces que un elemento específico aparece en la lista
# conteo = lista.count(3)

# Ordenar la lista en orden ascendente
# lista.sort()

# Invertir el orden de los elementos en la lista
#lista.reverse()

#print(lista)
#print(conteo)

# Lista con Lista [1,2,3,[4,5,'cadena',['nueva cadena']]]

Lista = [1,2,3,[4,5,'cadena',['nueva cadena']]]
# print(Lista[3][3][0])
############################ Diccionarios  ###################################

datos = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "profesión": "Ingeniero"
}

# Indexar en diccionarios

diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
#print(diccionario['edad'])

# Obtener una lista con todas las claves del diccionario
# claves = diccionario.keys()

# Obtener una lista con todos los valores del diccionario
# valores = diccionario.values()

# Obtener el valor asociado a una clave específica
# edad = diccionario.get('edad') # hacer esto es equivalente a diccionario['edad']

# Eliminar una clave y su correspondiente valor del diccionario
#del diccionario['ciudad']

# Eliminar todos los elementos del diccionario
# diccionario.clear()
#print(diccionario)

########################### Tuplas ####################################

# Es un tipo de dato inmutable con elementos entre paréntesis separados por comas
t1 = (1,2,3)
# print(t1)

####################### Operadores logicos y condicional if ###############################
# """
# # Ejemplo de operadores lógicos en Python
# x = 1
# y = 16
# z = 15
#
# # Operador and
# if x < y and y < z:
#     # print("x es menor que y y y es mayor que z")
#
# # Operador or
# if x > y or y > z:
#     # print("x es mayor que y o y es mayor que z")
#
# # Operador not
# if not(x == y):
#     # print("x no es igual a y")
#
# # El condicional 'if' (si)
# """x=2
# if x<3:
#     print('Es menor')"""
#
# # Else
# """x=4
# if x<3:
#     print('Es menor')
# else:
#     print('Es mayor')"""
#
# #Elif
# """x=3
# if x<3:
#     print('Es menor')
# elif x==3:
#     print('Es igual')
# else:
#     print('Es mayor')

# Ciclos

############################# Bucle for #################################
# for(int i = 0; i < 10; i++){}
# str_2 = 'Hola como estan'
# list_2 = [1, 'hola', 7.0]
# for i in list_2:
#     print(i)

# for i in range(5, 10): # (v_inicial, v_final)
#     print(i)
#
# for i in range(10): # (v_final)
#     print(i)

# for i in range(20, 51, 2): # (v_inicial, v_final, paso)
#     print(i)
# valor_final = 10
# for i in range(1, valor_final):
#     print(i)

############################# Bucle while #################################
# while True:
#     print("hola")

# while (condicional):
############################# Funciones #####################################
# def myFun(num):
#     aux = num**2
#     return aux
#
# def myfun2():
#     print("Hola a todos")
#
# x = myFun(2)
#
# print(x)
#
# myfun2()

# print(myFun(7.0))
############################# Funciones Lambda ################################

# fl = lambda var:var**2
# print(fl(4))
# print(fl(2))


# x = lambda a, b, c : a + b + c
# print(x(1,2,3))