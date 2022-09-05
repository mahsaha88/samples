import numpy as np
x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
y = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])
print("add=", np.add(x, y))
print("subtract=", np.subtract(x, y))
print("multiple=", np.multiply(x, y))
print("divide=", np.divide(x, y))
print("power:", np.power(x, 2))
print("remainder:", np.remainder(x, 5))