#2- Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de
#horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a
#seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um
#caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$ 37,50

qntd_Horas = int (input("Digite a quantidade de horas trabalhadas:"))
turno = input ("Digite seu turno: ")
if (turno == "Noturno"):
    valorhora = 45.00
else:
    valorhora = 37.50
salario = qntd_Horas * valorhora
print ("O valor do seu salário é de: ", salario)