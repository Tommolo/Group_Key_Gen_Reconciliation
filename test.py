from share_key_between_alice_and_bob_with_eve.all_common_values import *

# Simulation parameters
num_of_probes = 200 #the number of signal send from alice to bob and viceversa
m = 3  # Shape parameter (typically m >= 0.5)
Omega = 1  # Scale parameter (mean power)
Pt = 10 # Power in Watts 
alpha = 2  # Path loss exponent normally in the range 2-4
noise_floor = 4*10**-14 # Noise floor in watts
num_dec_values = 2 # Number of the decimal values

# Distances in meters
d_ab = 1  # Distance between Alice and Bob
d_ae = 2  # Distance between Alice and Eve
d_be = 2 # Distance between Bob and Eve

# Correlation coefficients
rho_Alice_Bob = 0.97
rho_Alice_Eve = 0.1
rho_Bob_Eve = 0.1

#number of iterations
iterations = 1000


all_common_values=compute_rss_common_values(iterations,num_of_probes,m,Omega,rho_Alice_Bob,rho_Alice_Eve,rho_Bob_Eve,Pt,d_ab,d_ae,d_be,alpha,noise_floor,num_dec_values)
print(len(all_common_values.get("all_common_values_ab_ba")))