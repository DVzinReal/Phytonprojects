# Lista com dados simulados de consumo de energia
leituras = [55, 63, 70, 95, 105]  

# Itera sobre cada leitura na lista
for leitura in leituras:
    # Verifica se a leitura de consumo excede o limite de 100 kW
    if leitura > 100:
        print(f"Alerta! Consumo de {leitura} kW excedeu o limite!")
    else:
        print(f"Consumo dentro do limite: {leitura} kW")