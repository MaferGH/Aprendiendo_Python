#Constantes

#Una constante es un nombre que, no puede ser reasignado una vez que se ha asignado por primera vez.
#En python no existe tal cosa, sin embargo podemos poner la nombre de una variable en mayuscula; esto para indicar una variable cuyo valor no debería cambiar durante la vida del programa.

IVA = 0.21
IVA_REDUCIDO = 0.1
IVA_SUPEREDUCIDO = 0.04

radio = float(input("Radio de la pizza en centimetros: "))
superficie = 3.1416 * radio ** 2
precio_final = superficie * 0.025 * (1 + IVA)
print("El precio final es", "$", precio_final)
