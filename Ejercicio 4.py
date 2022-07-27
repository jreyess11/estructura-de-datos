import msvcrt
import random
import statistics

# @author Jose Reyes

N = int(input("Ingrese la cantidad de números: "))
num = []

for i in range(N):
    num.append(random.randint(1, 100))

print(f"Sus números al azar son: {str(num)[1:-1]}")
print(f"El mayor número generado es: {max(num)}")
print(f"El promedio de todos los números es: {statistics.mean(num)}")
msvcrt.getch()
