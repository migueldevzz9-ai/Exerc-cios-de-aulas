#4- Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor desses
#valores. Utilize o comando de repetição que desejar.

positivos = 0
negativos = 0
temZero = False

#verificar números positivos e negativos
for i in range(10):
    num = float(input("Digite um número: "))
    if num > 0:
     positivos += 1
    elif num < 0:
     negativos += 1
    else:
       temZero = True
if temZero:
   print (f"A quantidade de numeros positivos é: {positivos} e de negativos é : {negativos} .\n Zero é um valor neutro, então ele não é nem positivo nem negativo.")
else:
  print (f"A quantidade de numeros positivos é: {positivos} e de negativos é : {negativos}")