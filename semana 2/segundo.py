#variables ejemplo 1 entero y decimal
#variables 
# 1.empezar por letra
# 2.no admite espacios en blanco  
# 3.puede incluir letras siempre que se respete la primera regla 
# 4. nombres auténticos
entero=10
decimal=3.14
print("El valor de la variable entero es:",entero)
print("El valor de la variable decimal es:",decimal)
print(f"El valor de la variable entero es: {entero}y el valor de la variable decimal es: {decimal}")
#Variables ejemplo 2 cadena de texto
cadena="hola, soy Jazmin y estudio sistemas computacionales"
print("El valor de la variable cadena es:",cadena)

#Ejemplo de un arreglo de enteros
aentero=[7,9,3,1,5]
print("El valor de la variable aentero es:",aentero)
print(f"el valor 1 de la variable aentero es: {aentero[0]}")
print(f"el valor 2 de la variable aentero es: {aentero[1]}")
print(f"el valor 3de la variable aentero es: {aentero[2]}")
print(f"el valor 4 de la variable aentero es: {aentero[3]}")
print(f"el valor 5 de la variable aentero es: {aentero[4]}")
#arreglo es estático y lista es dinámica

#Ejemplo de una lista de métodos
lista=[]
print("Valores de la lista:", lista)

#Agregar elementos a la lista
lista.append(10)
lista.append(6)
lista.append(2)
print("Valores de la lista:", lista)

#Lista método extend() agrega múltiples elementos a la lista
lista.extend([1,2,3,9,10,11,80])
print("Valores de la lista:", lista)
#el método append() agrega un solo elemento a la lista, mientras que el método extend() agrega 
# múltiples elementos a la lista.

#Lista ejemplo sort() ordena los elementos de la lista en orden ascendente
lista.sort()
print("Valores de la lista ordenados:", lista)

#Lista con diferentes tipos de datos
directorio=[1,20,"Hola",3.14,True]
print("Valores de la lista directorio:", directorio)

#Ejemplo de una estructura de datos 
miestructura={
    "nombre":"Jazmin",
    "direccion":"Calle 123",
    "telefono":"555-1234",
}
print("Estructura de datos:", miestructura)
print("Nombre:", miestructura["nombre"])
print("Dirección:", miestructura["direccion"])
print("Teléfono:", miestructura["telefono"])

miarrayestructura=[
    {
        
        "nombre":"Jazmin",
        "direccion":"Calle 123",
        "telefono":"555-1234",
    },
    {
        "nombre":"Juan",
        "direccion":"Calle 456",
        "telefono":"555-5678",
    },
    {
        "nombre":"María",
        "direccion":"Calle 789",
        "telefono":"555-9012",
    },
    {
        "nombre":"Pedro",
        "direccion":"Calle 012",
        "telefono":"555-3456",
    },
    
]
print("Mostrar todos los datos de mi arreglo de estructuras:", miarrayestructura)
print("Mostrar el nombre de la primera estructura:", miarrayestructura[0]["nombre"],miarrayestructura[0]["telefono"])
