#Explicación

#Con la función random lo que hacemos es llamar caracteres aleatorios, con la cantidad le decimos que sean 8 y lo que hace es combinarlos al azar.

import random #Se corrige la palabra Random ya que le faltaba una letra
import string

def generar_contraseña(longitud=8): #Se define la función ya que le faltaba el DEF
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

contraseña_generada = generar_contraseña(8) 


print(f" La contraseña es: {contraseña_generada}") #Se agrega esta parte para que al momento de imprimir nos indique el texto completo 

