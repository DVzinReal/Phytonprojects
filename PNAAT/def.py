'''
# função exibe temperatura
def exibir_temperatura(temp):
    print("Temperatura atual:", temp)

# chamada
exibir_temperatura(27)
'''


#função calcular média
def calcular_media(a,b):
    return(a + b) / 2

# chamada
print("Média:", calcular_media(25, 20))

#função verifica vibração com parâmetro limite = 30
def alerta_vibracao(valor, limite=30):
    if valor > limite:
        return "⚠️ vibração excessiva detectada!"
    return "Tudo Normal."

#chamadas
print(alerta_vibracao(45)) #acima do limite
print(alerta_vibracao(20)) #abaixo do limite