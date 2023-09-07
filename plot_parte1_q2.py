import numpy as np
import matplotlib.pyplot as plt

# data
x = np.array([54, 123, 5, 203, 97])
y = np.array([7.5, 8.5, 2.0, 9.8, 8.0])

# linear regression
a, b = np.polyfit(x, y, 1)

# plot
plt.plot(x, y, 'o')
plt.plot(x, a*x + b)
plt.xlabel('Número de exercícios resolvidos')
plt.ylabel('Média final')
plt.show()
