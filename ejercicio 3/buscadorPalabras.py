def contar_palabra(texto, palabra):
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto . Este texto tiene palabras repetidas."
palabra= "texto"

print(f"La palabra '{palabra}' aparece {contar_palabra(texto, palabra)} veces:")
