import numpy as np 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
data = np.loadtxt('na-22.tsv',skiprows = 26)
modified_data = []
n=1
for i in range(n,len(data[:,2])-n):
	modified_data.append(np.mean(data[:,2][i-n:i+n]))




plt.semilogy(data[:,1][0:-2*n][20:-1],modified_data[20:-1],'.')
plt.title("Smoothed via rolling 10 point average")
plt.xlabel('Energy (KeV)')
plt.ylabel("Counts")
# plt.savefig('Sr-90Smoothed.png')
plt.show()