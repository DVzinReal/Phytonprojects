python = {"Ana", "Carlos", "Joao", "Maria", "Pedro"}
dados = {"Maria", "Pedro", "Lucas", "Julia"}

print("Nos dois cursos:", python & dados)

print("Apenas python:", python - dados)

print("Apenas dados:", dados - python)

print("Pelo menos um curso:", python | dados)

print("Total de alunos distintos:", len(python | dados))

