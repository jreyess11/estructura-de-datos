import msvcrt
import random

# @author Jose Reyes

A = []

for i in range(20):
    A.append(random.randint(0, 10))

print(f"El vector A es: {A}")
print("\nORDENANDO")

for j in range(19, -1, -1):
    if A[j] == 0:
        A.remove(A[j])
        A.append(0)


print(f"El nuevo vector A (ceros al final) es: {A}")

msvcrt.getch()
