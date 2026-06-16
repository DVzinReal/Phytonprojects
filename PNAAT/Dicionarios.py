#Dicionario mutavel
sensor = {"id": 101, "tipo": "temperatura", "valor": 23.5}

#Criação e inicialização de um dicionário para armazenar estados de máquinas:
estados_maquinas = {
    "maquina_1": "operacional", 
    "maquina_2": "manutencao", 
    "maquina_3": "parada", 
    "maquina_4": "operacional",
    "maquina_7": "quebrada"
}

#Adicionando novos estados ao dicionário (simulando novas máquinas):
estados_maquinas.update({"maquina_5": "operacional"})
estados_maquinas.update({"maquina_6": "manutencao"})
print(f"Estados após adicionar novas máquinas: {estados_maquinas}")

#Acessando estados específicos:
estado_maquina_1 = estados_maquinas["maquina_1"]
estado_maquina_3 = estados_maquinas["maquina_3"]
print(f"O estado da máquina 1 é: {estado_maquina_1}")
print(f"O estado da máquina 3 é: {estado_maquina_3}")

#Modificando um estado:
estados_maquinas["maquina_2"] = "operacional"  # Supondo que a máquina 2 voltou a operar
print(f"Estados após atualização: {estados_maquinas}")

#Removendo um estado:
del estados_maquinas["maquina_3"]  # Remove o estado da máquina 3 (desativada)
print(f"Estados após remover uma máquina: {estados_maquinas}")

#Verificando o tamanho do dicionário:
print(f"Número total de estados registrados: {len(estados_maquinas)}")

#Listando todas as máquinas cadastradas:
print(f"Máquinas atualmente registradas: {estados_maquinas.keys()}")

#Definindo um dicionário de comandos para as máquinas:
comandos_maquinas = {
    "maquina_A": ["ligar", "monitorar", "desligar"], 
    "maquina_B": ["manutencao", "calibrar"], 
    "maquina_C": ["ligar", "monitorar"], 
    "maquina_D": ["ligar", "desligar"]
}
print(f"\nComandos para as máquinas: {comandos_maquinas}")

#Executando o próximo comando para a máquina A:
proximo_comando = comandos_maquinas["maquina_A"].pop(0)
print(f"Executando comando: {proximo_comando} para a máquina A")
print(f"Comandos restantes para a máquina A: {comandos_maquinas['maquina_A']}")