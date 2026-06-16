#Parte 2 – Loop for: Iterando com range(), lista e dicionário
#Exemplo 1 – Usando for com range()
#O for com range() é usado quando sabemos quantas vezes queremos repetir algo.

# O loop irá iterar de 1 a 5, representando cada ciclo de consumo
for ciclo in range(1, 6):
    # Cálculo do consumo de energia para o ciclo atual
    consumo = 50 + (ciclo * 8)
    # Exibe o ciclo e o respectivo consumo de energia em kW
    print(f"Ciclo {ciclo}: Consumo de energia = {consumo} kW")
    # O loop irá gerar valores de 1 a 9, pulando de 2 em 2
for ciclo in range(1, 10, 2):  # A cada dois valores
    print(ciclo)  # Exibe o valor atual do ciclo