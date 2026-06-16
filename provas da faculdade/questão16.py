dados = """
001;Ana;F;8.5
002;Carlos;M;6.0
003;Maria;F;9.2
004;Joao;M;erro
005;Pedro;M;7.5
006;Julia;F;10.0
007;Lucas;M;5.5
"""

alunos = []

for linha in dados.strip().split("\n"):
    codigo, nome, sexo, nota = linha.split(";")

    try:
        nota = float(nota)

        alunos.append({
            "codigo": codigo,
            "nome": nome,
            "sexo": sexo,
            "nota": nota
        })
    
    except:
        continue

notas = [a["nota"]for a in alunos]

media = sum(notas) / len(notas)

ordenadas = sorted(notas)

mediana = ordenadas[len(ordenadas)//2]

minimo = min(notas)
maximo = max(notas)
amplitude = maximo - minimo

print(media)
print(mediana)
print(minimo)
print(maximo)
print(amplitude)

contagem = {}

for aluno in alunos:
    sexo = aluno["sexo"]
    contagem[sexo] = contagem.get(sexo, 0) + 1

print(contagem)

for sexo in ["F", "M"]:
    notas_sexo = [a["nota"] for a in alunos if a["sexo"] == sexo]
    media_sexo = sum(notas_sexo) / len(notas_sexo)
    print(sexo, media_sexo)

aprovados = [a for a in alunos if a["nota"] >= 7]
print(aprovados)

ordenados = sorted(
    alunos,
    key=lambda a: a["nota"],
    reverse=True
)

print(ordenados)

print(f"{'Codigo':<8}{'Nome':<10}{'Sexo':<6}{'Nota':<6}")

for aluno in alunos:
    print(
        f"{aluno['codigo']:<8}"
        f"{aluno['nome']:<10}"
        f"{aluno['sexo']:<6}"
        f"{aluno['nota']:<6.1f}"
        )
