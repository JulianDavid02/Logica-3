#Explicación

#Se establece input en los float para que permitiera realizar la operación al momento de ingresar los símbolos.
# Se corrige las variables num ya que al faltarle un letra - número, el código al momento de compilar no lo encontraba.
#Se agrega return para que devolviera el resultado



def calculadora():
    num1 = float(input("Ingrese el primer número: ")) # Se agrega input en los float
    num2 = float(input("Ingrese el segundo número: ")) # Se agrega input en los float
    operacion = input ("Ingrese la operación (+, -, *, /): ")
    
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2 # Se corrige las variables num
    elif operacion == '*':
        resultado = num1 * num2 # Se corrige las variables num
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = "Operación no válida"

    return print(resultado) # Se agrega return en el print y se elimina el segundo texto "resultado"

calculadora() # La palabra calculadora al final estaba mal escrita.







