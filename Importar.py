#Los modulos o bibliotecas permiten agregar a nuestro programa nuevas herramientas, objetos o funciones.
#Para usar cualquier modulo debemos usar la palabra import seguida del modulo deseado
#import MODULO_NOMBRE

#El modulo time trabaja con fechas y horas y este tiene una funcion llamada asctime() que retorna la fecha actual

import time  #Aquí estamos importando el modulo
fecha = time.asctime() #agregamos una variable que será igual a la función llamada
print(fecha)

#Para poder cambiar el nombre de un modulo se hace de la siguiente manera.

import time as date
fecha2 = date.asctime()
print = (fecha2)

#A este tipo de casos le llamamos espacios de nombres.
#Podemos tener variables y funciones con el mismo nombre y lo respetará por el modulo que tenemos.


