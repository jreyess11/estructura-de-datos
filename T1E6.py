import msvcrt
import random

# @author Jose Reyes

A = []
B = []
C = []

for i in range(10):
    A.append(random.randint(200, 1000))
    B.append(random.randint(200, 1000))

C = A[:]
print(f"El vector A es: {A}")
print(f"El vector B es: {B}")
print("\nORDENANDO")

for j in range(9, -1, -1):
    if (B[j] % 2) == 0:
        A[j] = B[j]
    else:
        A.remove(A[j])

for j in range(9, -1, -1):
    if (C[j] % 2) == 0:
        B.remove(B[j])
    else:
        B[j] = C[j]


print(f"El nuevo vector A (números pares de B) es: {A}")
print(f"El nuevo vector B (números impares de A) es: {B}")

msvcrt.getch()
