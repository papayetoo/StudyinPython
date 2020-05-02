import numpy as np

num = 16
result = np.array([np.random.randint(0,10) for _ in range(num**2)]).reshape((num,num))
print(num)
for row in range(num):
    print(*result[row])