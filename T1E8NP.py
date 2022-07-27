import msvcrt
import numpy as np

# @author Jose Reyes

patron = np.empty([9,9], dtype=str)

for i in range(9):
    for j in range(9):
        patron[i][j] = "-"
        if j == 4 or i == 4:
            patron[i][j]="o"

print(patron)
msvcrt.getch()
