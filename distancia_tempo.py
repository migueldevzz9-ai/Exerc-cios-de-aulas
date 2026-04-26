#4- Elabore um programa para calcular a velocidade de três objetos diferentes (com velocidade constante).
#Conhecemos (são dados digitados pelo usuário), para cada objeto, a distância percorrida e o tempo que necessitou para percorrer essa distância.
#Utilize um método geral que calcule e retorne a velocidade de um objeto, fornecidos como parâmetros os dados de distância e tempo.

calcular_velocidade = lambda distancia, tempo: distancia / tempo

# OBJETO 1
distancia1 = float(input("Distância do objeto 1: "))
tempo1 = float(input("Tempo do objeto 1: "))

# OBJETO 2
distancia2 = float(input("Distância do objeto 2: "))
tempo2 = float(input("Tempo do objeto 2: "))

# OBJETO 3
distancia3 = float(input("Distância do objeto 3: "))
tempo3 = float(input("Tempo do objeto 3: "))

# Cálculo velocidade
velocidade1 = calcular_velocidade(distancia1, tempo1)
velocidade2 = calcular_velocidade(distancia2, tempo2)
velocidade3 = calcular_velocidade(distancia3, tempo3)

# Resultado
print(f"Velocidade do objeto 1: {velocidade1}")
print(f"Velocidade do objeto 2: {velocidade2}")
print(f"Velocidade do objeto 3: {velocidade3}")