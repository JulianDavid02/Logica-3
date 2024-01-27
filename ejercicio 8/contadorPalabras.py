def contar_palabras_en_archivo(nombre_archivo): #Se agregan los dos puntos al final
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read( )
            palabras = contenido.split( )
            return len(palabras)
    except FileNotFoundError:
            return (f"El archivo {nombre_archivo} no fue encontrado.") #Se corrige la palabra return

nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
print(f"El archivo contiene {contar_palabras_en_archivo(nombre_archivo)} palabras.")
