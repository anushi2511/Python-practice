import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints)
plt.show()

plt.plot(ypoints, marker='*')
plt.show()

plt.plot(ypoints, 'o:r')
plt.show()

plt.plot(ypoints, marker = 'o', ms = 10, mec = 'r', mfc = 'b')
plt.show()

plt.plot(ypoints, ls = ':')

plt.plot(ypoints, c = '#4CAF50')
plt.show()

plt.plot(ypoints, linewidth = '10.5')
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)
plt.show()