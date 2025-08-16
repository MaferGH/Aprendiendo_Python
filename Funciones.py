#Funciones

#Print es la funcion principal que Python pone a nuestra disposición.
#Además de permitirnos usar más argumentos.

print("hola",
    "cómo estás",
    ":)") #hola cómo estás :)

#Tambien muestra numeros enteros, como:

print(5, 6) #5 6

print(5, "prueba") #5 prueba

#Y podemos agregar más variables

name = "Fernanda"
lastname = "García"

print(name, lastname) #Fernanda García

#Funcion que retorna resultado es input
# input() detiene la ejecución del programa y espera a que se introduxca un texto y se pulse la tecla enter

nombre = input("Escribe tu nombre:")
print("Se ha escrito un nombre:")
print(nombre)
