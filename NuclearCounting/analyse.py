import numpy as np 
import matplotlib.pylab as plt

#import the data
data = np.transpose(np.loadtxt('data.txt', skiprows = 1))

LL     = data[0]
energy = data[0]/8*.662
counts = data[2]

#----- Plot Lower level vs Counts -----
plt.plot(data[0],counts,'bo')
plt.xlabel("Lower Level +/- .02")
plt.ylabel("counts +/- 1")
plt.title("CS 137 Radiation Distrobution")
plt.savefig("LL_v_Counts.png")
plt.close()
#----------

#----- plot Energy vs counts -----
plt.plot(energy,counts,'bo')
plt.xlabel("Energy +/- .003 (MeV)")
plt.ylabel("counts +/- 1")
plt.title("CS 137 Radiation Distrobution")
plt.savefig("Energy_v_Counts.png")
plt.close()
#----------

#computed fit parameters
a1 = 1545
a2 = .658
a3 = .038
a4 = 0
a5 = 0

#calculate gaussian fit curve
x   = np.linspace(.5,.8,100)

def fit(x):
	return a1*np.e**(-(x-a2)**2/(2*a3**2))+a4*x+a5
#----- plot the photopeak and fit -----
plt.plot(x,fit(x))
plt.plot(energy[2:19],counts[2:19],'bo')

plt.xlabel("Energy +/- .003 (MeV)")
plt.ylabel("counts +/- 1")
plt.title("CS 137 Photopeak")
plt.savefig("CS137Photopeak.png")
plt.close()
#----------

S = 0
for i in range(len(energy[2:19])):
	print counts[2:19][i]
	print(energy[2:19][i])
	print fit(energy[2:19][i])
	S+=(counts[2:19][i]-fit(energy[2:19][i]))**2/(counts[2:19][i])
	
print S/(17-5)