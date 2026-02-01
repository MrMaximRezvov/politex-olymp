import numpy as np

a = int(input())
b = int(input())

a = a * np.pi / 180

b = b * np.pi / 180

print(-((np.sin(a) * (np.cos(b) - np.cos(a))) / (np.sin(b) - np.sin(a))) + np.cos(a))