import msvcrt
import random

# @author Jose Reyes

azar = []

for i in range(20):
    azar.append(random.randint(15, 86))

print(f"El primer vector generado es: {azar}")
print(f"El vector ordenado (descendente) es: {sorted(azar, reverse=True)}")

msvcrt.getch()
