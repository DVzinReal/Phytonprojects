from math import hypot

cateto1 = float(input("Digite o primeiro cateto: "))
cateto2 = float(input("Digite o segundo cateto: "))

hipotenusa = hypot(cateto1, cateto2)

print(f"{hipotenusa:.2f}")
