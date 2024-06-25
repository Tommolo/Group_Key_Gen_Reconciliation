import numpy as np
from scipy.stats import nakagami
import matplotlib.pyplot as plt
import math
import marcumq
from scipy.special import gammainccinv
from scipy.optimize import fsolve

def generate_nakagami_m_channel(m, Omega):
    # Generate Nakagami-m distributed magnitudes
    magnitudes = nakagami.rvs(m, scale=np.sqrt(Omega), )
    return magnitudes

# Example parameters
num_samples = 128
m = 3 # Shape parameter (typically m >= 0.5)
Omega = 10  # Scale parameter (mean power)
Ptx = 10 # Power transmission in dBm
d_ab = 50  # Distance in meters
d_ae = 100  # Distance in meters
alpha = 2  # Path loss exponent

# Generate h_ba channel coefficient
h_ba = generate_nakagami_m_channel(m, Omega)



# Generate h_ae channel coefficient
h_ae = generate_nakagami_m_channel(m, Omega)

eps = np.random.normal(loc=0, scale=1, size=num_samples)

# Compute the cross-correlation
rho = 0.95 # Example correlation coefficient

# Update h_ab based on h_ba and eps
h_ab = (rho * h_ba) + (1 - math.pow(rho,2)*eps)**1/2


# Calculate RSSI for Alice (gamma_ab) and Bob (gamma_ba)
gamma_ab = (Ptx + abs(h_ab)** 2 * d_ab **-alpha)
gamma_ba = (Ptx + abs(h_ba)** 2 * d_ab **-alpha)
gamma_ae = (Ptx + abs(h_ae)** 2 * d_ae **-alpha)


# Algorithm to generate RSS at Bob
#for i in range (0,len(gamma_ba)-1):
 #   rss_bob=np.array(len(gamma_ba)-1)
  #  a= np.sqrt((2*m*p*gamma_ab[i])/np.mean(gamma_ab)*(1-p))
   # b= np.sqrt((2*m*gamma_ab)/np.mean(gamma_ab)*(1-p))
    #r=np.random.rand()
    #rss_bob = 1 - marcumq.marcumq(1,a,b)

#print(rss_bob)

# Applica la funzione a ciascun numero nel set
cleaned_numbers_ab = np.round(gamma_ab,4)
cleaned_numbers_ba = np.round(gamma_ba,4) 
cleaned_numbers_ae = np.round(gamma_ae,4) 

list1=[]
list2=[]
list3=[]

for element in cleaned_numbers_ab:
    list1.append(element)

for element in cleaned_numbers_ba:
    list2.append(element)

for element in cleaned_numbers_ae:
    list3.append(element)

print(list1)
print(list2)
print(list3)

set1=set(list1)
set2=set(list2)
set3=set(list3)

intersection = set1.intersection(set2)
intersection2 = set1.intersection(set3)

print(intersection,len(intersection))
print(intersection2,len(intersection2))

# Plot RSSI values
plt.figure(figsize=(10, 6))
plt.plot(gamma_ba, label='Alice', color='green', marker='x')
plt.plot(gamma_ab, label='Bob', color='blue', marker='o')
plt.plot(gamma_ae, label='Eve', color='red', marker='^')
plt.title('RSSI Channel Probes')
plt.xlabel('Sample Index')
plt.ylabel('RSS')
plt.legend()
plt.grid(True)
plt.show()
