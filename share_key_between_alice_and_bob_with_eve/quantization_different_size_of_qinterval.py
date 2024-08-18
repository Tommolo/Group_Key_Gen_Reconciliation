from all_common_values import generate_channel_coefficients
import numpy as np
import matplotlib.pyplot as plt


# Number of iterations
num_iterations = 1
count_subset = 0

set_ab_length=[]
SI_list_ab = []
SI_list_be = []
average_length_ab= []
average_length_ba= []

def quantization_by_indexes_alice(channel_coefficients,quantization_intervals):
    quantization_by_indexes=[]
    for i in range(0,len(channel_coefficients)):
        if channel_coefficients[i] >= quantization_intervals[2] or channel_coefficients[i] < quantization_intervals[1]:
            quantization_by_indexes.append(i)
    return quantization_by_indexes



def quantization_by_indexes_bob(channel_coefficients,quantization_intervals):
    quantization_by_indexes=[]

    for i in range(0,len(channel_coefficients)):
        if channel_coefficients[i] >= quantization_intervals[4]  or channel_coefficients[i] < quantization_intervals[0]:
           quantization_by_indexes.append(i) 
    return quantization_by_indexes


for _ in range(num_iterations):
    # Generate channel coefficients
    channel_coefficients = generate_channel_coefficients(1000, 0.9, 0.1, 0.1)


    h_ab = channel_coefficients.get("h_ab")
    h_ba = channel_coefficients.get("h_ba")
    h_be = channel_coefficients.get("h_be")

    # Ensure h_ab and h_ba are numpy arrays or lists
    h_ab = np.array(h_ab.real)  # Convert to numpy array
    h_ba = np.array(h_ba.real)  # Convert to numpy array
    h_be = np.array(h_be.real) 
    # Determine the minimum and maximum values of the array
    min_val_ba = h_ba.min()
    max_val_ba = h_ba.max()

    min_val_ab = h_ab.min()
    max_val_ab = h_ab.max()

    # Calculate the quantization intervals
    quantization_intervals_ba = np.linspace(min_val_ba, max_val_ba, num=6)
    quantization_intervals_ab = np.linspace(min_val_ab, max_val_ab, num=6)

    indexes_ba=quantization_by_indexes_alice(h_ba,quantization_intervals_ba)
    indexes_ab = quantization_by_indexes_bob(h_ab,quantization_intervals_ab)
    indexes_be = quantization_by_indexes_bob(h_be,quantization_intervals_ab)

    print(indexes_ba)
    print(indexes_ab)
    print(indexes_be)


    average_length_ab.append(len(indexes_ab))
    average_length_ba.append(len(indexes_ba))
    if(len(indexes_ab)!=0):
        SI_ab = len(set(indexes_ba).intersection(set(indexes_ab)))/len(set(indexes_ab))
        SI_list_ab.append(SI_ab)
        if(SI_ab==1):
             set_ab_length.append(len(set(indexes_ab)))

    

    if(len(indexes_be)!=0):
        SI_be = len(set(indexes_ba).intersection(set(indexes_be)))/len(set(indexes_be))
        SI_list_be.append(SI_be)
       


print(SI_list_ab.count(1)/num_iterations)
print(SI_list_be.count(1)/num_iterations)

count_when_is_greater_than_32 = len([num for num in set_ab_length if num >= 32])

print(count_when_is_greater_than_32/num_iterations)

plt.figure(figsize=(10, 6))
plt.plot(h_ba.real, marker='^', linestyle='-', color='r', label='H_ba')
plt.plot(h_ab.real, marker='o', linestyle='-', color='b', label='H_ab')
#plt.plot(h_be.real, marker='^', linestyle='-', color='r', label='h_be')

plt.axhline(np.mean(h_ba), color='y', linestyle='--',label='Alice_mean')
plt.axhline(np.mean(h_ab), color='g', linestyle='--',label='Bob_mean')

plt.axhline(quantization_intervals_ab[0], color='b', linestyle='--')
plt.axhline(quantization_intervals_ab[1], color='b', linestyle='--')
plt.axhline(quantization_intervals_ab[2], color='b', linestyle='--')
plt.axhline(quantization_intervals_ab[3], color='b', linestyle='--')
plt.axhline(quantization_intervals_ab[4], color='b', linestyle='--')
plt.axhline(quantization_intervals_ab[5], color='b', linestyle='--')


plt.axhline(quantization_intervals_ba[0], color='r', linestyle='--')
plt.axhline(quantization_intervals_ba[1], color='r', linestyle='--')
plt.axhline(quantization_intervals_ba[2], color='r', linestyle='--')
plt.axhline(quantization_intervals_ba[3], color='r', linestyle='--')
plt.axhline(quantization_intervals_ba[4], color='r', linestyle='--')
plt.axhline(quantization_intervals_ba[5], color='r', linestyle='--')


#plt.axhline(maximum_be.real, color='r', linestyle='--',label='Eve')
#plt.axhline(minimum_be.real, color='r', linestyle='--')

plt.legend()
plt.title('Channel coefficients samples')
plt.xlabel('Samples')
plt.ylabel('channel coefficients')
plt.grid(True)
plt.show()

