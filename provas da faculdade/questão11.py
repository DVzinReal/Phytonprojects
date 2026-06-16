texto = """
Python e simples.
Python e poderoso.
Programar em Python e divertido.
"""

linhas = texto.strip().split("\n")

print("Linhas:", len(linhas))

palavras = texto.split()
print("Palavras:", len(palavras))

contador = palavras.count("Python")
print("Python aparece:", contador)

maior = max(palavras, key=len)
print("Maior palavra:", maior)
