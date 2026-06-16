notas = [8.5 , 7.0 , 9.0 , 5.5 , 6.0 , 10.0 , 4.5]
media = sum(notas) / len(notas)

maior = max(notas)

menor = min(notas)

aprovadas = [nota for nota in notas if nota >= 7]

percentual_aprovacao = (len(aprovadas) / len(notas)) * 100

print(f"A media da turma foi: {media:.2f}")

print(f"A maior nota da turma foi: {maior} e a menor foi: {menor}")

print(f"Notas aprovadas: {aprovadas}")

print(f"o percentual de aprovação foi: {percentual_aprovacao:.2f}")



