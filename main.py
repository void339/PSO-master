from math import sin

from pso_minmax import PSO
import matplotlib.pyplot as plt

def demo_func(x):
    x1, x2 = x
    return -(sin(x1)+sin(x2))

pso = PSO(func=demo_func, dim=2, pop=5, max_iter=5, lb=[-10,-10], ub=[10,10], w=0.8, c1=0.5, c2=0.5)
pso.run()
print('best_x is ', pso.gbest_x, 'best_y is', pso.gbest_y)

import matplotlib.pyplot as plt

plt.plot(pso.pbest_y)
plt.show()