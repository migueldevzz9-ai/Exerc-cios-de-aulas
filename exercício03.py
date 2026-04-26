#3- Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar
#o valor da compra considerando o desconto, conforme descrito abaixo: 
#para compras acima de R$ 200 a loja dá um desconto de 20%
#para as abaixo disso não tem desconto, mostre o valor da compra.

valor_compra = float (input("Digite o valor da sua compra: "))
desconto = valor_compra * 0.20
valor_final = valor_compra - desconto
if (valor_compra > 200):
    print("O total do seu desconto é:", desconto)
    print ("Com o desconto sua compra ficou:", valor_final)
else:
    print("Você não possui desconto, o valor da sua compra é de:", valor_compra)