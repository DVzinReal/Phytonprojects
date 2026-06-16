import random

alunos = ["barak obama", "vladimir putin", "lula", "sei la to sem ideia"]
posicoes = ["Primeiro", "Segundo", "Terceiro", "Quarto"]

random.shuffle(alunos)

for indice, aluno in enumerate(alunos):
    lugar = posicoes[indice]
    print(f"O {lugar} sorteado foi: {aluno}")