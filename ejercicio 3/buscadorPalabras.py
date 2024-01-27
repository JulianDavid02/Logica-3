#Explicación
#Lo que hace el código es detectar cadenas de texto que estén juntas y devolverme el número de veces que se repiten
def contar_palabra(texto, palabra): #Se agregan los dos puntos del final
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto . Este texto tiene palabras repetidas."
palabra= "texto" #Se cambia el nombre de la palabra para que al imprimir la identifique 

print(f"La palabra '{palabra}' aparece {contar_palabra(texto, palabra)} veces:")
