#3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
#Crie uma programa que permita digitar o nome do produto e valor da compra, e
#imprimindo o nome do produto e o valor da venda.
#Valor de compra Valor de venda
#valor < R$10,00 lucro de 70%
#R$ 10,00 <= valor < R$ 30,00 lucro de 50%
#R$ 30,00 <= valor < R$ 50,00 lucro de 40%
#valor >= R$50,00 lucro de 30%

produto = (input("Digite o nome do produto: "))
valor = float(input("Digite o valor do produto: "))

if valor <= 10:
    venda = valor * 1.70
elif valor <= 30:
    venda = valor * 1.50
elif valor <= 50:
    venda = valor * 1.40
else:
    venda = valor * 1.30
print (f"O {produto} foi vendido por {venda}")