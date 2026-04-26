#2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo
#grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou zero);
#  a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a zero.

import math
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
raizdelta = (B**2 - 4 * A * C)
if A==0:
    print("Como A é igual a 0, não é uma equação de segundo grau")
elif raizdelta<0:
    print("Não há raízes reais")
else:
    x1 = (-(B) + math.sqrt(raizdelta)) / 2 *A
    x2 = (-(B) - math.sqrt(raizdelta)) / 2 *A
    print("É possível realizar a equação")
    print(f"O valor de x1 é: {x1}")
    print(f"O valor de x2 é: {x2}")