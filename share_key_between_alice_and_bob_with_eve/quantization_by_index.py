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

        if alpha==0.65:
            found = True
            break
        elif min_index < max_index:
            min_index += 1
            max_index -= 1
        else:
            break

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

        elif min_index < max_index:
            min_index += 1
            max_index -= 1
        else:
            break

    return indexes,alpha,min_index,max_index
    

def get_dict_alpha_indexes(channel_coefficients):
    dict_alpha_indexes = {}
    min_index = 0
    max_index = len(set(channel_coefficients)) - 1

    # Target alpha values
    target_alphas = [0.5, 0.6, 0.7, 0.8, 0.9]
    
    while len(dict_alpha_indexes) < len(target_alphas):
        indexes = quantization_by_indexes(channel_coefficients, min_index, max_index)
        alpha = (len(channel_coefficients) - len(indexes)) / len(channel_coefficients)

        # Add to the dictionary if alpha is one of the target values
        if alpha in target_alphas and alpha not in dict_alpha_indexes:
            dict_alpha_indexes[alpha] = indexes

        elif min_index < max_index:
            min_index += 1
            max_index -= 1
        else:
            break

    return dict_alpha_indexes

        




    
