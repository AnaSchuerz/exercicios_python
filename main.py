import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1000)
z = np.cos(x)

plt.plot(x, z)
plt.savefig("plot3.png", dpi=300)
plt.show()
