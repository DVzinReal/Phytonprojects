saldo = 100
valor = 20

def sacar(x, y):
    if x >= y:
        x = x - y
    return x   
print(sacar(saldo, valor))

    