import numpy as np

def quantization_by_indexes(channel_coefficients,min_index,max_index):
    # Sort and remove duplicates
    channel_coefficients_ordered = sorted(set(channel_coefficients))
    indexes = [] 
    for i in range(len(channel_coefficients)):

        if  channel_coefficients[i]<=channel_coefficients_ordered[min_index] or channel_coefficients[i] >= channel_coefficients_ordered[max_index] :  # Compare with the m-th element
            indexes.append(i)

    return indexes



def get_indexes_according_to_alpha_Alice_value(channel_coefficients):
    alpha = 0
    found = False
    indexes = []
    min_index = 0
    max_index = len(set(channel_coefficients)) -1

    while not found:
        indexes = quantization_by_indexes(channel_coefficients, min_index, max_index)
        alpha = (len(channel_coefficients) - len(indexes)) / len(channel_coefficients)

        if 0.5 <= alpha <= 0.65:
            found = True
            break
        elif 0 <= min_index <= len(set(channel_coefficients)) and 0 <= max_index <= len(set(channel_coefficients)):
            min_index += 1
            max_index -= 1

    return indexes,alpha,min_index,max_index
    

def get_indexes_according_to_alpha_Bob_value(channel_coefficients):
    alpha = 0
    found = False
    indexes = []
    min_index = 0
    max_index = len(set(channel_coefficients))-1

    while not found:
        indexes = quantization_by_indexes(channel_coefficients, min_index, max_index)
        alpha = (len(channel_coefficients) - len(indexes)) / len(channel_coefficients)

        if 0.85 <= alpha <= 0.9:
            found = True
            break
        elif 0 <= min_index <= len(set(channel_coefficients)) and 0 <= max_index <= len(set(channel_coefficients)):
            min_index += 1
            max_index -= 1

    return indexes,alpha,min_index,max_index
    

    
