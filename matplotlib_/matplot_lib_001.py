import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

xpoints = range(4)
ypoints = np.array([3, 8, 1, 10])
zpoints = np.array([x**2 for x in xpoints])

plt.plot(zpoints, ypoints, 'p--g', ms=20, mec='r')
plt.show()
