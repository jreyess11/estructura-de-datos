import msvcrt
# @author Jose Reyes

cant = int(input("Ingrese la cantidad de numeros a leer: "))
ln = []
r = 0

while r < cant:
    num = int(input(f"Ingrese el número {r + 1}: "))
    ln.append(num)
    r = r + 1

ln.sort()
print(f"El mayor número leído es {max(ln)} y se repite {ln.count(max(ln))} veces")

msvcrt.getch()
