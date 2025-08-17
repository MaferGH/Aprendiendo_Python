#La funcion id retorna el identificador del objeto que le pasamos como argumento

saludo = "Hola, que tal"
print(id(saludo)) #4375231600

saludo = "Hola mundo"
hola = saludo
print(id(saludo))
print(id(hola))



valor1 = 2000
valor2 = 2000

print(id(valor1))
print(id(valor2))

a = 2 * 10 + 1
b = 2 * 10 + 1

print(id(a))
print(id(b))
