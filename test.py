import numpy as np
import matplotlib.pyplot as plt
#Создай пирамиду и отбрази её через pyplot
n = 5
a = np.zeros((n, n))
for i in range(n):
    for j in range(i + 1):
        a[i, j] = i - j + 1
print(a)
plt.imshow(a, cmap='gray')