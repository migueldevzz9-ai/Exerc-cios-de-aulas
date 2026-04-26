#1- Faça um método que receba como parâmetros o Km inicial, Km final, quantidade de
#litros gastos e preço do litro. Calcule e mostre:
#- Distância percorrida;
#- Consumo médio;
#- Valor gasto;
#Faça um programa principal que solicite para o usuário o valor da quilometragem inicial,
#final, a quantidade de litros gastos e o preço do litro e mostre a distância percorrida, o
#consumo médio e o valor gasto, para isso utilize o método definido acima.

kmi=float(input("KM inicial: "))
kmf=float(input("KM final: "))
litros=float(input("Litros gastos: "))
preçoLitro=float(input("Preço do litro: "))

def calculo(kminicial,kmfinal,litros,preçolitro):
    distancia = kmfinal - kminicial
    print(f"Distancia = {distancia}")
    consumo = distancia / litros
    print(f"Consumo médio = {consumo}")
    gasto = litros * preçolitro
    print(f"Gasto toal = {gasto}")

calculo(kmi,kmf,litros,preçoLitro)