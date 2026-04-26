#2- Escreva um método com retorno que receba como parâmetros os lados de um
#retângulo, calcula e retorna o valor de sua área.
#area = lado*lado
#Faça um programa principal que solicite os valores dos lados de um retângulo ao usuário,
#e utilizando a função definida acima, calcule e mostre o valor de área.

def area_Retangulo(lado1,lado2):
    area = lado1 * lado2
    return area
lado1=int(input("Digite o valor do lado 1: "))
lado2=int(input("Digite o valor do lado 2: "))
print(f"A área do retângulo é: {area_Retangulo(lado1,lado2)}")