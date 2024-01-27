def factorial(n): #Se agregan los dos puntos
    if n == 0 or n == 1: #Se agrega signo igual y dos puntos
        return 1 #Se corrigue la palabra return
    else:
        return n * factorial(n - 1) #Se corrige la palabra return

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")
