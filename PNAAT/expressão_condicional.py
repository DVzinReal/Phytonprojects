# Defina as variáveis x = 10, y = 20, z = 30
# Execute a expressão condicional:
# (x < y and y > z) or (x + y == z and not (z == x * 3))
# Determine se a expressão retorna True ou False

def verificar():
    x = 10
    y = 20
    z = 30
    return (x < y and y > z) or (x + y == z and not (z == x * 3))

resultado = verificar()
