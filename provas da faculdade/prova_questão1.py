# Aluno: Davi Marinho Donato


casos_novos = [
    2, 5 , 9 , 15 , 22 , 34 , 51 , 73 , 98 , 120 ,
    135 , 141 , 138 , 127 , 110 , 92 , 75 , 60 , 47 , 36 ,
    27 , 20 , 14 , 10 , 7 , 5 , 3, 2, 1, 1 
]

#a) Casos acumulados
# Calcula o total acumulado de casos dia a dia
casos_acumulados = []
soma = 0

for bro in range(30):               # percorre os 30 dias (índices 0 a 29)
    soma = soma + casos_novos[bro]  # adiciona os casos do dia atual
    casos_acumulados.append(soma)   # guarda o acumulado até este dia
    print(soma)                     # exibe cada acumulado

# Dias específicos para consultar os acumulados (índices)
dias = [1, 7, 14, 21, 29]

for dia in dias:
    print(f"Dia {dia}: casos acumulados:{casos_acumulados[dia]}")

#b) Pico de casos novos 
# Encontra o maior valor da lista e seu índice (dia em que ocorreu)
pico = max(casos_novos)
dia_pico = casos_novos.index(pico)   # .index retorna a primeira ocorrência do valor
print(f"Pico: dia {dia_pico} com {pico} casos novos.")

#c) Fases de ascensão e descensão
# Divide a lista em duas partes: antes/durante o pico e depois do pico
crescimento = casos_novos[0:dia_pico + 1]   # do dia 0 até o pico (inclusive)
queda = casos_novos[dia_pico + 1:]          # do dia seguinte ao pico até o fim

print(f"Tamanho da fase de ascensão: {len(crescimento)} dias")
print(f"Tamanho da fase de descensão: {len(queda)} dias")

#d) Variação dia a dia 
# Calcula a diferença entre cada dia e o anterior (crescimento ou queda)
variacao = [
    casos_novos[bro] - casos_novos[bro - 1]
    for bro in range(1, 30)          # começa do dia 1 pois o dia 0 não tem anterior
]

maior_crescimento = max(variacao)
maior_queda = min(variacao)          # valor negativo representa queda
print(f"o maior crescimento é {maior_crescimento}")
print(f"a maior queda é {maior_queda}")

#e) Média móvel de 7 dias 
# Calcula a média dos últimos 7 dias (incluindo o dia atual)
media_movel = []

for bro in range(30):
    if bro < 6:                       # primeiros 6 dias não têm 7 dias completos
        media_movel.append(None)      # coloca None para indicar dado insuficiente
    else:
        janela = casos_novos[bro - 6 : bro + 1]   # pega os 7 dias (índices bro-6 até bro)
        media = sum(janela) / 7                    # calcula a média
        media_movel.append(media)

dias = [6, 13, 20, 29]               # dias (índices) para exibir a média móvel
for dia in dias:
    print(f"Dia {dia}: {media_movel[dia]:.2f}")