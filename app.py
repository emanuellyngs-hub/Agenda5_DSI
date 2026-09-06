# Programa de cálculo de média de notas
# Autor: Emanuelly Nicolly

# Entrada
nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0,75

# Saída
print(f"\nAparelho: {nome}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")

# Classificação
if consumo_mensal < 50:
    print("Classificação: Baixo consumo - Econômico!")
elif consumo_mensal < 150:
    print("Classificação: Consumo moderado")
else:
    print("Classificação: Alto consumo - Considere alternativas!")