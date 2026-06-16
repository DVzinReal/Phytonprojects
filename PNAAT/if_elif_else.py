temperatura = float(input("Digite a temperatura do sistema: "))
if temperatura > 25:
    print("Acionar ventilação")
elif temperatura < 15:
    print("Aquecer ambiente")
else:
    print("Sistema estável")