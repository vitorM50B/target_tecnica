import json

# Abrindo arquivo
with open("dados.json", "r", encoding="utf-8") as f:
    faturamento = json.load(f)

# Filtrar, maneira simples
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Calcular
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
