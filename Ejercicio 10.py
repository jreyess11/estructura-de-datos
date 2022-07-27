import msvcrt
import statistics

# @author Jose Reyes

N = int(input("Ingrese la cantidad de bultos: "))
total = 0
i = 0
tarifa = 0
bultos = []

while total < N:
    peso = int(input(f"Ingrese el peso del bulto #{i + 1} (kg): "))
    if peso > 0:
        if peso <= 500:
            bultos.append(peso)
            if sum(bultos) <= 18000:
                if 25 < peso <= 300:
                    tarifa = tarifa + 1500 * peso
                if 300 < peso <= 500:
                    tarifa = tarifa + 2500 * peso
                total = total + 1
                i = i + 1
            else:
                bultos.remove(bultos[i])
                des = int(input("\nLo sentimos, este bulto excede el tamaño máximo de carga (18.000 kg). "
                                 f"Por el momento su peso es {sum(bultos)} kg. \n"
                                 "Oprima 1 si desea agregar otro bulto de menor tamaño o 0 para terminar la lista: "))
                if des == 0:
                    total = N
                else:
                    print()
        else:
            print("Recuerde que un bulto no puede exceder los 500 kg")
    else:
        print("Por favor ingrese un peso válido.")

USD = tarifa/4407.48

print(f"\nEl peso final de la carga es {sum(bultos)} kg, con un total de {len(bultos)} bultos.")
print(f"El peso del bulto más pesado es {max(bultos)} kg y del menor es {min(bultos)} kg.")
print(f"El peso promedio de los bultos es {statistics.mean(bultos)} kg.")
print(f"El precio final de la carga es COP ${tarifa:,.0f} // USD ${USD:,.2f}")

msvcrt.getch()
