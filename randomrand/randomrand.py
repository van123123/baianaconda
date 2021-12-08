import numpy as np
a = np.random.rand()
b = np.random.rand(4)
c = np.random.rand(2, 3)
print("a = ", a)
print("b = ", b)
print("c = ", c)
g = np.random
g.seed(10)
 
print("g rand: ", g.rand())
e = np.random
e.seed(10)
 
print("e rand: ", e.rand())
m, sigma = 0, 0.1
s = np.random.normal(m, sigma, size=5)
print(s)
np.random.randn(3, 3)
print(np.random.randn(3, 3))
sigma * np.random.randn(3, 3) + m
np.random.uniform(low=0.0, high=1.0, size=None)
u = np.random.uniform(size=4)
print(u)
p=np.random.permutation(10)
print(p)