#6 - Ler uma quantidade indeterminada de alunos com as seguintes informações RGM, NOME, Sexo e Media.
#Calcular a media da sala, exibir a media da sala, maior nota, menor nota e a media por sexo.

soma = 0
quantidade = 0
maior = 0
menor = 10

# mulheres
qtdMulheres = 0
somaMulheres = 0

# homens
qtdHomens = 0
somaHomens = 0

for i in range(6):
    print(f"\n aluno {i+1}")

    sexo = input("Qual é seu sexo: M/F ").upper()
    nome = input("Digite seu nome: ").upper()
    RGM = int(input("Digite seu RGM: "))
    media = float(input("Digite sua média: "))

    # soma geral
    soma += media
    quantidade += 1

    # maior e menor
    if i == 0:
        maior = media
        menor = media
    else:
        if media > maior:
            maior = media
        if media < menor:
            menor = media

    # sexo 
    if sexo == "M":
        somaHomens += media
        qtdHomens += 1
    elif sexo == "F":
        somaMulheres += media
        qtdMulheres += 1

mediaSala = soma / quantidade

print(f"Resultados: \n Media da sala: {mediaSala} \n Maior nota: {maior} \n Menor nota: {menor}")

if qtdHomens > 0:
    print(f"Média de homens: {somaHomens/qtdHomens}")

if qtdMulheres > 0:
    print(f"Média de mulheres: {somaMulheres/qtdMulheres}")