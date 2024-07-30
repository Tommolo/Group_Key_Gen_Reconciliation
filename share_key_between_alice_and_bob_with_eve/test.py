from all_common_values import generate_channel_coefficients
from quantization_by_index import *
import numpy as np

# Number of iterations
num_iterations = 100
count_subset = 0

for _ in range(num_iterations):
    # Generate channel coefficients
    channel_coefficients = generate_channel_coefficients(600, 0.9, 0.1, 0.1)

    h_ab = channel_coefficients.get("h_ab")
    h_ba = channel_coefficients.get("h_ba")
    

    # Ensure h_ab and h_ba are numpy arrays or lists
    h_ab = np.array(h_ab.real)  # Convert to numpy array
    h_ba = np.array(h_ba.real)  # Convert to numpy array

    # Calculate mean-max and mean-min distances
    mean_ab = np.mean(h_ab)
    delta_max_ab = (np.max(h_ab) - np.mean(h_ab))
    delta_min_ab = (np.mean(h_ab) - np.min(h_ab)) 

    delta_max_ba = np.max(h_ba) - np.mean(h_ba) 
    delta_min_ba = (np.mean(h_ba) - np.min(h_ba)) / 20

    max_ba = get_max(h_ba, 0)
    min_ba = get_min(h_ba, delta_min_ba)

    max_ab = get_max(h_ab, delta_max_ab)
    min_ab = get_min(h_ab, delta_min_ab)

    index_quantization_ba = index_quantization(h_ba, delta_max_ba, delta_min_ba)
    index_quantization_ab = index_quantization(h_ab, delta_max_ab, delta_min_ab)


    print(index_quantization_ab, len(index_quantization_ab))
    print(index_quantization_ba,len(index_quantization_ba))
    # Check if index_quantization_set_ab is a subset of index_quantization_set_ba
    if set(index_quantization_ab).issubset(set(index_quantization_ba)):
        count_subset += 1

print("Number of times index_quantization_set_ab is a subset of index_quantization_set_ba:", count_subset)
