#4- Elabore um programa em Python que implemente uma calculadora com as funções de
#somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
#valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e mostrar o resultado.

n1 = int(input("Digite o valor de n1: "))
n2 = int(input("Digite o valor de n2: "))
escolha = int(input(" 1 = Soma \n 2 = Subtração \n 3 = multiplicação \n 4 = divisão \n Qual operação deseja realizar? "))

if escolha == 1:
    soma = n1 + n2
    print(f"A soma de {n1} e {n2} fica igual a: {soma}")
elif escolha == 2:
    subtração = n1 - n2
    print(f"A subtração de {n1} e {n2} fica igual a: {subtração}")
elif escolha == 3:
    multiplicação = n1 * n2
    print(f"A multiplicação de {n1} e {n2} fca igual a: {multiplicação}")
elif escolha == 4:
    n2  == 0
    print("Erro, não é possivel fazer a divisão por 0")
else:
    divisão = n1 / n2
    print(f"A divisão de {n1} e {n2} fica igual a: {divisão}")
          