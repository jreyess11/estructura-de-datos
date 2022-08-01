import msvcrt

# @author Jose Reyes

N = int(input("Ingrese la cantidad de números primos: "))
cont = 0
x = 1
primos = []


def primo(n):
    for i in range(2, int(n/2)):
        if (n % i) == 0:
            return False
    return True


while cont < N:
    x = x + 1
    if primo(x):
        primos.append(x)
        cont = cont + 1

print(f"Los primeros {N} números primos son {str(primos)[1:-1]}")
msvcrt.getch()
