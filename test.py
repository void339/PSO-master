import numpy as np
def demo_func(x):
        x1, x2, x3 = x
        return x1 ** 2 + x2 ** 2 + x3 ** 2


def func_transformed(X):
        return np.array([demo_func(x) for x in X])


X = np.random.uniform(low=[0, -1, 0.5], high=[1, 1, 1], size=(2, 3))
print(X)
print(func_transformed(X))