cores = ["azul", "Verde", "Vermelho", "Verde"]

# Cores pelo nome do valor
cores.remove("Verde")
print(cores) # ['Azul', 'Vermelho', 'verde'] (so tirou o primeiro)

#Remove pelo indice usando del 
del cores[1]
print(cores) #['Azul', 'Verde']