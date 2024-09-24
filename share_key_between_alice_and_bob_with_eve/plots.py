import matplotlib.pyplot as plt
import numpy as np

# Construct and the realtive guard band for h_ba,h_ab and h_be
def quantization_plot(h_ba,h_ab,h_be,min_index_A,max_index_A,min_index_B,max_index_B,min_index_E,max_index_E):

    h_ba_ordered = sorted(set(h_ba))
    h_ab_ordered = sorted(set(h_ab))
    h_be_ordered = sorted(set(h_be))

    plt.figure(figsize=(10, 6))
    plt.plot(h_ba, marker='o', linestyle='-', color='blue', label='H_ba')
    plt.plot(h_ab, marker='^', linestyle='-', color='black', label='H_ab')
    plt.plot(h_be, marker='d', linestyle='-', color='red', label='H_be')


    plt.axhline(h_ba_ordered[min_index_A], color='blue', linestyle='--')
    plt.axhline(h_ba_ordered[max_index_A], color='blue', linestyle='--')

    plt.axhline(h_ab_ordered[min_index_B], color='black', linestyle='--')
    plt.axhline(h_ab_ordered[max_index_B], color='black', linestyle='--')


    plt.axhline(h_be_ordered[min_index_E], color='red', linestyle='--')
    plt.axhline(h_be_ordered[max_index_E], color='red', linestyle='--')

    plt.legend()
    plt.title('Channel coefficients samples')
    plt.xlabel('Samples')
    plt.ylabel('channel coefficients')
    plt.grid(True)
    plt.show()

def all_levels_of_quantization (h_ba):

    plt.figure(figsize=(10, 6))
    plt.plot(h_ba.real, marker='o', linestyle='-', color='blue', label='H_ba')

    for value in h_ba:
        plt.axhline(value, color='red', linestyle='--')    

    plt.legend()
    plt.title('All levels')
    plt.xlabel('Samples')
    plt.ylabel('channel coefficients')
    plt.grid(True)
    plt.show()

def plot_si_when_increase_alpha (alphas,si):

    plt.figure(figsize=(10, 6))
    plt.plot(alphas,si,marker ='^',color='blue')

    #plt.legend()
    plt.xlabel('alpha(a_A = 0.65)')
    plt.ylabel('Similarity of indexes (SI)')
    plt.grid(True)
    plt.show()

 