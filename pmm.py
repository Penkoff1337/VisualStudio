import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats
# from matplotlib import cm

dx = 0.05 # Шаг по x
dy = 0.05 # Шаг по y
a = 1.0
b = 1.0

x = np.arange(0,a+dx,dx).round(3) # Массив с отрезками x
y = np.arange(0,b+dy,dy).round(3) # Массив с отрезками y
nx = len(x) # Количество шагов по x
ny = len(y) # Количество шагов по y

# Создание массивов для расчета
U = np.zeros((nx, ny))
p = np.zeros((nx, ny))

# Граничные условия
for i in range (1, ny):
    U[(ny-1),i] = (i * dy - (i * dy)**2) * np.exp(i * dy) # Справа
    U[0,i] = (i * dy - (i * dy)**2) # Слева

for i in range (1, nx):
    U[i,(nx-1)] = (i * dx - (i * dx)**2) # Сверху
    U[i,0] = (i * dx - (i * dx)**2) # Снизу

maxit = 500 # Максимальное количество итераций

for iteration in range (0, maxit):
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            U[i, j] = 0.25 * (U[i + 1][j] + U[i - 1][j] + U[i][j + 1] + U[i][j - 1]) + dx * dx / 4 * ((i * dx)**2 - (j * dy)**2 - i * dx + j * dy)     

X, Y = np.meshgrid(x,y)

# Сохранение X, Y и U в один текстовый файл
data = np.column_stack((X.flatten(), Y.flatten(), U.flatten()))
np.savetxt('решение_уравнения_Пуассона.txt', data, fmt='%.4f', delimiter='\t', header='X\t\tY\t\tU', comments='')

# plt.suptitle('Решение уравнения Пуассона')
# plt.contourf(X, Y, U, 30, cmap='viridis')
# plt.colorbar()
# plt.show()
