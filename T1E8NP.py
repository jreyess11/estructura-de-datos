import msvcrt
import numpy as np

# @author Jose Reyes

patron = np.empty([9,9], dtype=str)

for i in range(9):
    for j in range(9):
        patron[i][j] = "-"
        if j == 4 or i == 4:
            patron[i][j]="o"
salida=""
for r in patron:
    for s in r:
        print(s, end="  ")
    print()

print(salida)
msvcrt.getch()
