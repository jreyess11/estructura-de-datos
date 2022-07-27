import msvcrt
import random
import statistics

# @author Jose Reyes

arr = []
tam = int(input("Ingrese el tamaño de su arreglo: "))

for i in range(tam):
    arr.append(random.randint(1, 50))

print(arr)

N = int(input("Ingrese el número a buscar en el arreglo: "))

if N in arr:
    print(f"¡El número {N} SI está en el arreglo!")
else:
    print(f"El número {N} NO está en el arreglo :(")

msvcrt.getch()
