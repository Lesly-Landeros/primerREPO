# escribir un programa que pida al usuario 2 numeros enteros y calcular la suma desde el numero 1 hasta el numero 2
#imprimir el resultado 

numero1= int(intput("ingrese un numero: "))
numero2= int(intput("ingrese un numero: "))

resultado= 0

for num in range (numero1, numero2 + 1):
resultado+=num

print(f'EL RESULTADO DE LA SUMA ES: {resultado}')

