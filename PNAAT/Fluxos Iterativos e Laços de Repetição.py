#Parte 1 – Loop while: Monitoramento contínuo
# Importando a biblioteca necessária para simular o tempo
import time

# Definindo o consumo de energia inicial
consumo_energia = 50  # Consumo inicial em kW
limite_superior = 100  # Limite superior de consumo seguro em kW

# Laço de repetição para monitorar o consumo de energia
while True:  
    print(f"Consumo de energia atual: {consumo_energia} kW")  
    if consumo_energia > limite_superior:
        print("Alerta: Consumo de energia acima do limite seguro!")
        break  # Sai do loop se o limite for ultrapassado

    # Simulando a variação do consumo de energia
    consumo_energia += 10  # Aumenta o consumo em 10 kW
    time.sleep(2)  # Pausa de 2 segundos entre as leituras

print("Monitoramento encerrado.")