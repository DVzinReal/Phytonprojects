# Simulação de leitura de pressão
pressao_atual = 3.5  # Pressão atual em bar
pressao_maxima = 5.0  # Pressão máxima permitida em bar
pressao_minima = 1.0  # Pressão mínima segura em bar

print(f'Pressão atual: {pressao_atual} bar')

# Lógica condicional para controle da pressão
if pressao_atual > pressao_maxima and pressao_atual > 4.0:
    print("Atenção: Pressão crítica! Acionando alívio de pressão.")
elif pressao_atual < pressao_minima or pressao_atual < 2.0:
    print("Atenção: Pressão muito baixa! Acionando compressor.")
else:
    print("Pressão dentro dos limites normais.")