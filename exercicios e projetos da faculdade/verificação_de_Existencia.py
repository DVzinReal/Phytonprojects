convidados = ["Joao", "Maria", "Carlos", "Pedro"]
nome = input("Digite seu nome: ")

if nome in convidados:
    print("pode entrar na festa!")
else:
    print("Nome não consta na lista.")

# Tambem podemos usar 'not in'
if "Pedro" not in convidados:
    print("Pedro faltou")