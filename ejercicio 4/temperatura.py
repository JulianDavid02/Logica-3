#Explicación
#Lo que hace el código es pedirnos ingresar la temperatura en celsius y con la fórmula matemática que corregimos lo convierte a Fahrenheit
def celsius_a_fahrenheit(celsius): #Se agregan los dos puntos al final
    return (celsius * 9/5) + 32 #Se agrega el + para que la fórmula funcione

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: ")) #Se agrega el input para que nos pida ingresar el texto
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
