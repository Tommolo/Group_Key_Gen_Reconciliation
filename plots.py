import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Construct and the realtive guard band for h_ba,h_ab and h_be
def quantization_plot(h_ba,h_ab,h_ae,min_index_A,max_index_A,min_index_B,max_index_B,min_index_E,max_index_E):

    h_ba_ordered = sorted(set(h_ba))
    h_ab_ordered = sorted(set(h_ab))
    h_be_ordered = sorted(set(h_ae))

    plt.figure(figsize=(10, 6))
    plt.plot(h_ba, marker='o', linestyle='-', color='blue', label='H_ba')
    plt.plot(h_ab, marker='^', linestyle='-', color='black', label='H_ab')
    plt.plot(h_ae, marker='d', linestyle='-', color='red', label='H_ae')


    plt.axhline(h_ba_ordered[min_index_A], color='blue', linestyle='--')
    plt.axhline(h_ba_ordered[max_index_A], color='blue', linestyle='--')

    plt.axhline(h_ab_ordered[min_index_B], color='black', linestyle='--')
    plt.axhline(h_ab_ordered[max_index_B], color='black', linestyle='--')


    plt.axhline(h_be_ordered[min_index_E], color='red', linestyle='--')
    plt.axhline(h_be_ordered[max_index_E], color='red', linestyle='--')

    plt.legend()
    plt.title('Channel coefficients samples')
    plt.xlabel('Samples')
    plt.ylabel('Re(channel coefficients)')
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

def plot_si_when_increase_alpha(alphas, si_b, si_e):
    plt.figure(figsize=(10, 6))
    plt.plot(alphas, si_b, marker='^', color='blue', label='SI for B')
    plt.plot(alphas, si_e, marker='o', color='red', label='SI for E')

    plt.legend()  # Added the legend to distinguish between the two plots
    plt.xlabel('Alpha (a_A = 0.6)')
    plt.ylabel('Similarity of Indexes (SI)')
    plt.grid(True)
    plt.show()



def adjusting_alpha_value(channel_coefficients,min_index,max_index):

    channel_coefficients_ordered = sorted(set(channel_coefficients))
    plt.figure(figsize=(10, 6))
    plt.plot(channel_coefficients, marker='o', linestyle='-', color='blue')

    plt.axhline(channel_coefficients_ordered[min_index], color='red', linestyle='--')
    plt.axhline(channel_coefficients_ordered[max_index], color='red', linestyle='--')
    
    plt.legend()
    plt.title('Channel coefficients samples')
    plt.xlabel('Samples')
    plt.ylabel('Re(channel coefficients)')
    plt.grid(True)
    plt.show()


def get_heatmap_alphas_SI(dict_alphas_SI,who):
   
   # Step 1: Extract unique x and y values
    x_vals = sorted(set(k[0] for k in dict_alphas_SI.keys()))
    y_vals = sorted(set(k[1] for k in dict_alphas_SI.keys()))


    # Step 2: Create a 2D grid (matrix) with NaN values
    data_matrix = np.empty((len(y_vals), len(x_vals)))
    data_matrix[:] = np.nan  # Initialize with NaN to mark missing values

    # Step 3: Populate the grid using the dictionary values
    for (x, y), value in dict_alphas_SI.items():
        x_idx = x_vals.index(x)
        y_idx = y_vals.index(y)
        data_matrix[y_idx, x_idx] = value

    # Step 4: Reverse y-axis labels for desired ordering
    y_vals_reversed = y_vals[::-1]  # Reverse the order of y values

    # Step 5: Plot the heatmap
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(
        data_matrix[::-1],  # Flip the matrix vertically
        vmin=0,
        vmax=1,
        annot=True,
        cmap='viridis',
        xticklabels=x_vals,
        yticklabels=y_vals_reversed
    )


    # Set labels and title
    if(who=="ab"):
         # Set the color bar label
        colorbar = heatmap.collections[0].colorbar
        colorbar.set_label('SI')
        plt.xlabel("alpha_alice")
        plt.ylabel("alpha_Bob")
        plt.title("Heatmap alphas Alice-Bob")
        plt.show()
     # Set labels and title
    elif(who=="ae"):
         # Set the color bar label
        colorbar = heatmap.collections[0].colorbar
        colorbar.set_label('SI')
        plt.xlabel("alpha_alice")
        plt.ylabel("alpha_Eve")
        plt.title("Heatmap alphas Alice-Eve")
        plt.show()
    # Set labels and title
    elif(who=="pr_ab"):
       # Set the color bar label
        colorbar = heatmap.collections[0].colorbar
        colorbar.set_label('Probability SI')
        plt.xlabel("alpha_alice")
        plt.ylabel("alpha_Bob")
        plt.title("Heatmap alphas Alice-Bob")
        plt.show()

    elif(who=="pr_ae"):
        colorbar = heatmap.collections[0].colorbar
        colorbar.set_label('Probability SI')
        plt.xlabel("alpha_alice")
        plt.ylabel("alpha_Eve")
        plt.title("Heatmap alphas Alice-Eve")
        plt.show()



def adjusting_alpha_value(channel_coefficients,min_index,max_index):

    channel_coefficients_ordered = sorted(set(channel_coefficients))
    plt.figure(figsize=(10, 6))
    plt.plot(channel_coefficients, marker='o', linestyle='-', color='blue')

    plt.axhline(channel_coefficients_ordered[min_index], color='red', linestyle='--')
    plt.axhline(channel_coefficients_ordered[max_index], color='red', linestyle='--')
    
    plt.legend()
    plt.title('Channel coefficients samples')
    plt.xlabel('Samples')
    plt.ylabel('Channel coefficients')
    plt.grid(True)
    plt.show()


def get_heatmap_alphas_bestN(dict_alphas_SI,min,max):
   
   # Step 1: Extract unique x and y values
    x_vals = sorted(set(k[0] for k in dict_alphas_SI.keys()))
    y_vals = sorted(set(k[1] for k in dict_alphas_SI.keys()))

    # Step 2: Create a 2D grid (matrix) with NaN values
    data_matrix = np.empty((len(y_vals), len(x_vals)))
    data_matrix[:] = np.nan  # Initialize with NaN to mark missing values

    # Step 3: Populate the grid using the dictionary values
    for (x, y), value in dict_alphas_SI.items():
        x_idx = x_vals.index(x)
        y_idx = y_vals.index(y)
        data_matrix[y_idx, x_idx] = value

    # Step 4: Plot the heatmap
    plt.figure(figsize=(8, 6))
    heatmap=sns.heatmap(data_matrix,vmin=min,vmax=max, annot=True, cmap='viridis',fmt='g', xticklabels=x_vals, yticklabels=y_vals)

    # Set the color bar label
    colorbar = heatmap.collections[0].colorbar
    colorbar.set_label('number of samples')
    plt.xlabel("alpha_alice")
    plt.ylabel("alpha_Bob")
    plt.title("Heatmap alphas bestN samples Alice-Bob")
    plt.show()


