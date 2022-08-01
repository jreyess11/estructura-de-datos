import msvcrt
import statistics
from prettytable import PrettyTable

# @author Jose Reyes

titulos = PrettyTable()
N = int(input("Ingrese la cantidad de bultos: "))
total = 0
i = 0
tabla = []
controlpeso=[]
info = []
controlpeso = []
controlprecio = []


def mytable(arr):
    titulos.field_names = ["Bulto #", "Peso", "Precio COP", "Precio USD"]
    for i in arr:
        titulos.add_row(i)
    return titulos


def tarifa(num):
    COP = 0
    if 25 < num <= 300:
        COP = COP + 1500 * peso
    if 300 < num <= 500:
        COP = COP + 2500 * peso
    return COP


while total < N:
    peso = int(input(f"Ingrese el peso del bulto #{i + 1} (kg): "))
    info = []
    if peso > 0:
        if peso <= 500:
            info.append(i + 1)
            info.append(peso)
            controlpeso.append(peso)
            if sum(controlpeso) <= 18000:
                C = tarifa(peso)
                U = (C / 4422.30)
                info.append(f"${C:,.0f}")
                info.append(f"${U:,.2f}")
                controlprecio.append(C)
                i = i + 1
                total = total + 1
            else:
                controlpeso.remove(controlpeso[len(controlpeso) - 1])
                info.clear()
                des = int(input("\nLo sentimos, este bulto excede el tamaño máximo de carga (18.000 kg). "
                                f"Por el momento su peso es {sum(controlpeso)} kg. \n"
                                "Oprima 1 si desea agregar otro bulto de menor tamaño o 0 para terminar la lista: "))
                if des == 0:
                    total = N
                else:
                    print()
        else:
            print("Recuerde que un bulto no puede exceder los 500 kg")
    else:
        print("Por favor ingrese un peso válido.")
    if info:
        tabla.append(info)

print("\n--CONTROL DE DATOS--\n" + str(mytable(tabla)))
print(f"\nEl peso final de la carga es {sum(controlpeso)} kg, con un total de {len(controlpeso)} bultos.")
print(f"El peso del bulto más pesado es {max(controlpeso)} kg y del menor es {min(controlpeso)} kg.")
print(f"El peso promedio de los bultos es {statistics.mean(controlpeso)} kg.")
print(f"El precio final de la carga es COP ${sum(controlprecio):,.0f} // USD ${sum(controlprecio) / 4422.30:,.2f}")

msvcrt.getch()
