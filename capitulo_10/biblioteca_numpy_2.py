import numpy as np

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]
a = np.array(l1)
b = np.array(l2)

print(l1 + l2)
print(a + b)
print(l1 * 2)
print(a * 5)

print(a * b)

m = np.array([[1, 2, 3],
              [4, 5, 6]])

n= np.array([[5, 7, 2]
             [4, 3, 9]])