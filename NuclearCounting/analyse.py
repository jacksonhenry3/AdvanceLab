import numpy as np 
import matplotlib.pylab as plt
data = np.transpose(np.loadtxt('data.txt', skiprows = 1))
plt.plot(data[0],data[2],'bo')
plt.show()