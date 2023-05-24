import numpy as np
import matplotlib.pyplot as plt

# Valores para x e y
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)

# Cria uma grade de coordenadas x e y
X, Y = np.meshgrid(x, y)

# Calcula o valor de z
Z = np.sqrt((X**2 - (9/4)*(Y - 9/4)**2)/9)

# Plota o gráfico em 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configura os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Exibe o gráfico
plt.show()
