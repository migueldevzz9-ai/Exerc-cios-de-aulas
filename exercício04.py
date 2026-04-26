#4- Escreva um programa em Python que solicite ao usuário os valores de três contas de
#consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é
#suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
#insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.

salario = float (input("Digite o valor do seu salário: "))
agua = float (input("Digite o valor da sua conta de água: "))
luz = float (input("Digite o valor da sua conta de luz: "))
telefone = float (input("Digite o valor da sua conta de telefone: "))
finaldomes = salario - agua - luz - telefone
if (salario > agua + luz + telefone):
    print ("Tá ganhando bem ein, pagou as contas e ainda sobrou: ", finaldomes)
else:
    print ("Gastou mais do que ganhou, vai ficar sem farra esse mês")