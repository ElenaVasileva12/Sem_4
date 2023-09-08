# Напишите функцию для транспонирования матрицы

import random


# создаем матрицу
def create_matrix(n: int, m: int):
    data = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(random.randint(0, 9))
        data.append(b)
    return data


n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))

a = create_matrix(n, m)
for i in a:
    print(i)
print()

for j in range(m):
    for i in range(n):
        print(a[i][j], end=" ")
    print()
