produtos = []
aprovados = []
reprovados = []
pendentes = []

for i in range(10):
    numero_serie = int(input(f"Digite o {i}° numero de série:"))
    status = int(input(f"Digite o status de qualidade para o produto {numero_serie} (1 = aprovado, 0 = reprovado, -1 = pendente): "))

    produtos.append((numero_serie, status))

for produto in produtos:
    numero_serie, status = produto

    if status == 1:
        aprovados.append(numero_serie)
    elif status == 0:
        reprovados.append(numero_serie)
    elif status == -1:
        pendentes.append(numero_serie)

print("\nProdutos Aprovados:", aprovados)
print("Produtos Reprovados:", reprovados)
print("Produtos Pendentes:", pendentes)