dados = """
Ana;8.5;7.0
Carlos;5.0;6.0
Maria;9.0;9.5
Joao;erro;7.0
Pedro;6.5;8.0
"""

alunos = []

for linha in dados.strip().split("\n"):
    nome, nota1, nota2 = linha.split(";")

    try:
        nota1 = float(nota1)
        nota2 = float(nota2)

        media = (nota1 + nota2) / 2

        situacao = "Aprovado" if media >= 7 else "Reprovado"

        alunos.append({
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media,
            "situacao": situacao
        })
    
    except:
        continue

media_geral = sum(a["media"] for a in alunos) / len(alunos)

aprovados = [a["nome"]for a in alunos if a["media"] >= 7]

print(alunos)
print("media geral:", media_geral)
print("Aprovados:", aprovados)