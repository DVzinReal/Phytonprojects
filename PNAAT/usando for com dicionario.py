# Dicionário contendo o consumo de energia em diferentes setores
consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}

# Itera sobre cada setor e seu respectivo consumo de energia
for setor, consumo in consumo_setores.items():
    # Determina o status do consumo com base no limite de 100 kW
    if consumo > 100:
      status = "acima do limite" 
    else:
      status = "dentro do limite"
    # Exibe o setor, o consumo e o status
    print(f"Setor: {setor} | Consumo: {consumo} kW – Status: {status}")