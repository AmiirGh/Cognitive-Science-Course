import numpy as np
Expected_values = np.empty((0, 2))

Expected_values = np.append(Expected_values, np.array([5, 2]).reshape(1, 2), axis=0)
Expected_values = np.append(Expected_values, np.array([3, 0]).reshape(1, 2), axis=0)
Expected_values = np.append(Expected_values, np.array([4, 10]).reshape(1, 2), axis=0)

mean_col1 = np.mean(Expected_values[:, 0][Expected_values[:, 0] != 0])
mean_col2 = np.mean(Expected_values[:, 1][Expected_values[:, 1] != 0])


print(Expected_values)
print(mean_col1)
print(mean_col2)
print(abs(-1))
