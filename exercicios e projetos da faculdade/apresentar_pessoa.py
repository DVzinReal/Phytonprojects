import random

grupos = {
    "GRUPO 1": ["Ana Helloyse", "Gabriela", "Jonatan Ferreira", "Francisco Ivo", "Elyel"],
    "GRUPO 2": ["Francisco Gonçalves", "Arthur Maciel", "Isaac", "Kaio", "João Pedro"],
    "GRUPO 3": ["Emely", "Beatriz Gomes", "Débora Serafine", "Kauan Matheus", "Brayan", "Bruna"],
    "GRUPO 4": ["João Victor", "Clarissa", "Adrielly", "Ian", "Iordan"],
    "GRUPO 5": ["Lucas", "Daniel", "Luann", "Karla", "Janaina"],
    "GRUPO 6": ["Johnata Ruan", "Renan", "Lucas", "Fernanda", "Laura"],
    "GRUPO 7": ["Davi Marinho", "Eugênio Genuino", "Andressa Vitoria", "Kauã Ferreira", "Ana Luiza"],
    "GRUPO 8": ["João Emanuel", "Eduardo Alcântara", "Jefferson Cesar", "David Wilker", "Gustavo Ferreira"]
}

print("🎲 Sorteio dos apresentadores por grupo:\n")

for grupo, membros in grupos.items():
    escolhido = random.choice(membros)
    print(f"{grupo}: {escolhido}")