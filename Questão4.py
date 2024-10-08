# Valores de faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento.values())

# Cálculo e exibição da porcentagem de cada estado
print("Porcentagem de participação por estado:")
for estado, valor in faturamento.items():
    participacao = (valor / faturamento_total) * 100
    print(f"{estado}: {participacao:.2f}%")
