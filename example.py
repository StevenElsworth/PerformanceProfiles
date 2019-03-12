import numpy as np
from PerformanceProfile import PerformanceProfile as pp

Algorithm1 = 100 + 40*np.random.randn(100,1)
Algorithm2 = 70 + 20*np.random.randn(100,1)
Algorithm3 = 110 + 30*np.random.randn(100,1)

A = np.hstack([Algorithm1, Algorithm2, Algorithm3])
pp(A, 10, alg_legend=['Algorithm1', 'Algorithm2', 'Algorithm3'], markevery=5)
