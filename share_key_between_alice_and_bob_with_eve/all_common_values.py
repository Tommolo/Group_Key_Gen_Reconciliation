import numpy as np
from scipy.stats import nakagami
import json

# Specify the path to your JSON file
file_path = r'C:\Users\pieru\Documents\Python\Group_Key_Gen_Reconciliation\share_key_between_alice_and_bob_with_eve\parameters.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

num_of_probes = data['simulation_parameters']['num_of_probes']
iterations = data['simulation_parameters']['iterations']
Omega = data['simulation_parameters']['Omega']
m = data['simulation_parameters']['m']
Pt = data['simulation_parameters']['Pt']
alpha = data['simulation_parameters']['alpha']
noise_floor = data['simulation_parameters']['noise_floor']
num_dec_values = data['simulation_parameters']['num_dec_values']



def generate_nakagami_m_channel():
        # Generate Nakagami-m distributed magnitudes
        magnitudes = nakagami.rvs(m, scale=Omega, size=num_of_probes)
        return magnitudes



def compute_rss_common_values(rho_Alice_Bob, rho_Alice_Eve, rho_Bob_Eve, d_ab, d_ae, d_be):
    # Initialize lists to store intersection lengths
    all_common_values_ab_ba = []
    all_common_values_ba_ae = []
    all_common_values_ba_be = []
    
    

    for _ in range(iterations):
        # Generate h_ba channel coefficient
        h_ba = generate_nakagami_m_channel()

        # Generate h_ae and h_be channel coefficients
        eps_ab = np.random.normal(loc=0, scale=1, size=num_of_probes)
        eps_ae = np.random.normal(loc=0, scale=1, size=num_of_probes)
        eps_be = np.random.normal(loc=0, scale=1, size=num_of_probes)

        # Compute the Nakagami coefficients from Bob's point of view (Bob to Alice and vice versa)
        h_ab = rho_Alice_Bob * h_ba + np.sqrt(1 - rho_Alice_Bob**2) * eps_ab

        # Compute the Nakagami coefficients from Eve's point of view (Alice to Eve and Bob to Eve)
        h_ae = rho_Alice_Eve * h_ba + np.sqrt(1 - rho_Alice_Eve**2) * eps_ae
        h_be = rho_Bob_Eve * h_ba + np.sqrt(1 - rho_Bob_Eve**2) * eps_be

        # Compute RSS (Received Signal Strength) samples in dBm for Alice and Bob in dBm
        gamma_ba = 10 * np.log10((Pt * np.abs(h_ba)**2 * d_ab**-alpha) / noise_floor) + 30
        gamma_ab = 10 * np.log10((Pt * np.abs(h_ab)**2 * d_ab**-alpha) / noise_floor) + 30

        # Compute RSS samples in dBm for Alice and Eve and Bob and Eve in dBm
        gamma_ae = 10 * np.log10((Pt * np.abs(h_ae)**2 * d_ae**-alpha) / noise_floor) + 30
        gamma_be = 10 * np.log10((Pt * np.abs(h_be)**2 * d_be**-alpha) / noise_floor) + 30

        # Round the values to two decimal places if needed
        gamma_ab = np.round(gamma_ab, num_dec_values)
        gamma_ba = np.round(gamma_ba, num_dec_values)
        gamma_ae = np.round(gamma_ae, num_dec_values)
        gamma_be = np.round(gamma_be, num_dec_values)

        print("Gamma_AB (dBm):", np.sort(gamma_ab))
        print("Gamma_BA (dBm):", np.sort(gamma_ba))
        print("Gamma_AE (dBm):", gamma_ae)
        print("Gamma_BE (dBm):", gamma_be)

        # Store the lengths of intersections
        all_common_values_ab_ba.append(len(set(gamma_ba).intersection(set(gamma_ab))))
        all_common_values_ba_ae.append(len(set(gamma_ba).intersection(set(gamma_ae))))
        all_common_values_ba_be.append(len(set(gamma_ba).intersection(set(gamma_be))))
    
    return {
        "all_common_values_ab_ba": all_common_values_ab_ba,
        "all_common_values_ba_ae": all_common_values_ba_ae,
        "all_common_values_ba_be": all_common_values_ba_be
    }

