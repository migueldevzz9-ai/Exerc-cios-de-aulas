#7 - Ler vários produtos (código, descrição, quantidade e valor) para uma venda, exibir a lista de produtos e o total da venda.

total = 0
for i in range(5):
    print(f"\nProduto {i+1}")

    codigo = int(input("Código: "))
    descricao = input("Descrição: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor unitário: "))

    subtotal = quantidade * valor
    total += subtotal

    print(f"Subtotal do produto: {subtotal:.2f}")

print(f"\nTotal da venda: {total:.2f}")