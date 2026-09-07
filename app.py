# Programa de cálculo de média de notas
# Autor: Emanuelly Nicolly

def calcular_media():
    print("=" * 50)
    print("⚡CALCULADORA DE CONSUMO ELÉTRICO")
    print("=" * 50)

# Entrada de dados com validação
nome_aparelho = input("Nome do aparelho:")
potencia = float(input("Qual é a potência do aparelho em watts (w):"))
horas_dia = float(input("Qual é o tempo médio de uso diário (horas):"))

# Processamento
consumo_mensal = (potencia * horas_dia * 30)/1000 #Convertendo para kWh
custo_estimado = consumo_mensal * 0.75 # R$ 0.75 por kWh

# Saída formatada
print("\n" + "=" * 50)
print("📊RESULTADO FINAL")
print("=" * 50)
print(f"🔌Nome do aparelho: {nome_aparelho}")
print(f"⏰Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"💰Consumo estimado: R$ {custo_estimado:.2f}")

#Situação com emojis
if custo_estimado <= 10: 
    situação = "🟢CONSUMO BAIXO"
elif custo_estimado <= 30:
    situação = "🟡CONSUMO MODERADO"
else:
    situação = "🔴CONSUMO ALTO"

print(f"📌Situação: {situação}")
print("=" * 50)
print("\n Obrigado por usar a Calculadora de Consumo Elétrico!")
