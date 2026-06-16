from math import sin, cos, tan, radians

angulo_graus = int(input("Digite o angulo: "))

angulo_rad = radians(angulo_graus)

seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")