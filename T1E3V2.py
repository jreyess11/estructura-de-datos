import msvcrt

# @author Jose Reyes

N = int(input("Ingrese la cantidad de números primos: "))
x = 2
primos = []


def primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

try:
    while True:
        if primo(x):
            primos.append(x)
            if (len(primos)==N):
                break
        x += 1
    print(f"Los primeros {N} números primos son {str(primos)[1:-1]}")
except:
    print("Ingrese un número válido!")


msvcrt.getch()
