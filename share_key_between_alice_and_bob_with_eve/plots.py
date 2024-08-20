import matplotlib.pyplot as plt
import numpy as np

# Construct and the realtive guard band for h_ba,h_ab and h_be
def quantization_plot(h_ba,h_ab,h_be,quantization_intervals_ab,quantization_intervals_be,quantization_intervals_ba):

    plt.figure(figsize=(10, 6))
    plt.plot(h_ba.real, marker='^', linestyle='-', color='black', label='H_ba')
    plt.plot(h_ab.real, marker='o', linestyle='-', color='b', label='H_ab')
    plt.plot(h_be.real, marker='d', linestyle='-', color='red', label='H_be')



    plt.axhline(quantization_intervals_ab[0], color='b', linestyle='--')
    plt.axhline(quantization_intervals_ab[4], color='b', linestyle='--')


    plt.axhline(quantization_intervals_be[0], color='r', linestyle='--')
    plt.axhline(quantization_intervals_be[4], color='r', linestyle='--')


    plt.axhline(quantization_intervals_ba[2], color='black', linestyle='--')
    plt.axhline(quantization_intervals_ba[3], color='black', linestyle='--')



    #plt.axhline(maximum_be.real, color='r', linestyle='--',label='Eve')
    #plt.axhline(minimum_be.real, color='r', linestyle='--')

    plt.legend()
    plt.title('Channel coefficients samples')
    plt.xlabel('Samples')
    plt.ylabel('channel coefficients')
    plt.grid(True)
    plt.show()


def plot_pr_si_1_when_rho_changes(rho_list,pr_si_1):
    
    plt.figure(figsize=(10, 6))
    plt.plot(rho_list,pr_si_1)

    #plt.legend()
    plt.xlabel('Correlation coefficient')
    plt.ylabel('Pr(SI=1)')
    plt.grid(True)
    plt.show()


def plot_pr_si_1_when_num_samples_changes(num_of_samples,pr_si_1):
    
    plt.figure(figsize=(10, 6))
    plt.plot(num_of_samples,pr_si_1,color='red')

    #plt.legend()
    plt.xlabel('Number of samples')
    plt.ylabel('Pr(SI=1)')
    plt.grid(True)
    plt.show()


def plot_pr_setB_is_greatereq_32(num_of_samples,pr_setB_greater_than_32):
    
    plt.figure(figsize=(10, 6))
    plt.plot(num_of_samples,pr_setB_greater_than_32)

    #plt.legend()
    plt.xlabel('Number of samples')
    plt.ylabel('Pr(setB>=32)')
    plt.grid(True)
    plt.show()