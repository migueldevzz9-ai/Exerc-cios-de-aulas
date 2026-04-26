#5- Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens
#separadamente. Utilize o comando de repetição que desejar

# HOMENS
somaHomens = 0
qtdHomens = 0

# MULHERES
somaMulheres = 0
qtdMulheres = 0

for i in range(10):
    # Validação do sexo
    while True:
        sexo = input("Digite seu sexo M/F: ").upper()

        if sexo == 'M' or sexo == 'F':
            break
        else:
            print("Digite um valor válido!!")

    altura = float(input("Digite sua altura: "))

    # Classificação
    if sexo == 'M':
        somaHomens += altura
        qtdHomens += 1
    elif sexo == 'F':
        somaMulheres += altura
        qtdMulheres += 1

# Média homens
if qtdHomens > 0:
    mediaHomens = somaHomens / qtdHomens
else:
    mediaHomens = 0

# Média mulheres
if qtdMulheres > 0:
    mediaMulheres = somaMulheres / qtdMulheres
else:
    mediaMulheres = 0

# Resultado final
print(f"A média de homens é {mediaHomens:.2f}")
print(f"A média das mulheres é {mediaMulheres: .2f}")