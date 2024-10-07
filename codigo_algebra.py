# Ingredientes dos sanduíches e suas quantidades
sanduiches = {
    'Três Queijos': {'Pão Brioche': 1, 'Carne Moída': 0.15, 'Muçarela': 0.065, 'Cheddar': 0.072, 'Bacon': 0, 'Catupiry': 0.32, 'Cebola': 0.05},
    'Chicken Burger': {'Pão Brioche': 1, 'Frango': 0.14, 'Muçarela': 0.055, 'Cheddar': 0, 'Bacon': 0.02, 'Catupiry': 0.3, 'Cebola': 0}
}

# Preços dos ingredientes nos supermercados
precos_mercados = {
    'Covabra': {
        'Pão Brioche': 2.00, 'Carne Moída': 28.97, 'Frango': 29.88, 'Muçarela': 58.89, 
        'Cheddar': 117.36, 'Bacon': 29.87, 'Catupiry': 68.00, 'Cebola': 4.96
    },
    'Jau Serve': {
        'Pão Brioche': 2.74, 'Carne Moída': 39.49, 'Frango': 23.99, 'Muçarela': 83.66, 
        'Cheddar': 114.51, 'Bacon': 57.90, 'Catupiry': 65.82, 'Cebola': 7.99
    }
}

# Função para calcular o custo total de cada sanduíche em um supermercado
def calcular_custo_sanduiche(sanduiche, mercado):
    total = 0
    for ingrediente, quantidade in sanduiche.items():
        total += precos_mercados[mercado][ingrediente] * quantidade
    return total

# Cálculo dos custos nos dois supermercados
custos_totais = {
    mercado: {
        sanduiche: calcular_custo_sanduiche(ingredientes, mercado) 
        for sanduiche, ingredientes in sanduiches.items()
    }
    for mercado in precos_mercados
}

# Exibir os custos totais
for mercado, custos in custos_totais.items():
    print(f"Custo total no {mercado}:")
    for sanduiche, custo in custos.items():
        print(f"  {sanduiche}: R${custo:.2f}")

# Adicionar margem de lucro de 70%
margem_lucro = 1.7
custos_com_lucro = {
    mercado: {sanduiche: custo * margem_lucro for sanduiche, custo in custos.items()}
    for mercado, custos in custos_totais.items()
}

# Exibir os custos com margem de lucro
print("\nCustos com margem de lucro (70%):")
for mercado, custos in custos_com_lucro.items():
    print(f"Com lucro no {mercado}:")
    for sanduiche, custo in custos.items():
        print(f"  {sanduiche}: R${custo:.2f}")
Explicação:
Entrada de dados: O código começa definindo os ingredientes de cada sanduíche e as quantidades usadas, assim como os preços dos ingredientes nos supermercados Covabra e Jau Serve.
Função de cálculo: A função calcular_custo_sanduiche calcula o custo total de um sanduíche em um supermercado, multiplicando o preço de cada ingrediente pela sua quantidade.
Cálculo dos custos totais: Usa-se a função anterior para calcular o custo total de cada sanduíche nos dois supermercados.
Margem de lucro: Adiciona-se uma margem de lucro de 70% ao custo total.
Exibição dos resultados: Exibe os custos totais e os custos com a margem de lucro de 70% para cada sanduíche em ambos os supermercados.
Este código permite que você modifique os preços dos ingredientes e refaça os cálculos automaticamente.