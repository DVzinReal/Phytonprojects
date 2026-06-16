#Lógica Condicional e Fluxos de Decisão
# Simulação de leitura de nível de líquido
nivel_litros = 50  # Nível atual do líquido em litros
nivel_maximo = 100  # Nível máximo permitido em litros
nivel_minimo = 20  # Nível mínimo seguro em litros

print(f'Nível atual do líquido: {nivel_litros} litros')

# Lógica condicional para controle do nível de líquido
if nivel_litros > nivel_maximo:
    print("Atenção: Nível do líquido acima do máximo! Acionando sistema de drenagem.")
elif nivel_litros < nivel_minimo:
    print("Atenção: Nível do líquido abaixo do mínimo! Acionando sistema de abastecimento.")
else:
    print("Nível do líquido dentro dos limites normais.")