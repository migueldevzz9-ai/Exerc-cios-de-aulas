#1- Escreva um algoritmo que solicite um número ao usuário. Caso seja digitado um valor
#entre 0 e 9, mostre: “valor correto”, caso contrário mostre: “valor incorreto”.

num = int (input("Digite um número entre 0 e 9: "))
if ((num>0) and (num <= 9)):
    print ("Correto")
else:
    print ("Erro, o valor não segue o que foi pedido!!")