#OBJETOS
#Los objetos almacenan datos (que dependerán de la clase de objeto) y que puede operar con esos datos.
#A los datos almacenados en ese objeto se les llama atributos.

#CLASES
#Una clase es una especie de plantilla a partir de la que definimos objetos.

#Cuand creamos un objeto a partir de su clase, decimos que estamos instanciando al objeto o creando una instancia de esa clase

#Algunos tipos de clase son, str (cadena de texto) o int (numero entero)

cadena = str(13)
print(cadena)

texto = "Este Es Un Ejemplo" .upper() #Aquí lo estamos convirtiendo en mayuscula
print(texto.islower()) #Aquí estamos validando que sea minuscula
print("todo esta en minuscula".islower())

#Metodo count
#El metodo count() de la clase str retorna el numero de veces que una subcadena aparece en la cadena.

cadena = "Dale banana a la mona"
resultados = cadena.count("na")
print(resultados)

#Más breve

print("Pablo clavo un clavito".count("a"))

#Los objetos de la clase int tienen un metodo bit_length() que nos dice cuántos bits son necesarios para representar ese número
longitud = (42).bit_length()
print(longitud)

numero = 23
print(numero.real)
print(numero.imag)

