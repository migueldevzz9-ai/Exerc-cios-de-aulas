#3- Faça um programa em Python que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma: S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n

num = int(input("Digite um número inteiro positivo: "))
soma = 0 

for i in range(1,num + 1):
    soma = soma + (1/i)
    print (f"Somando 1/{i} -> soma atual {soma}")
print (f"Resultado final: {soma}")
