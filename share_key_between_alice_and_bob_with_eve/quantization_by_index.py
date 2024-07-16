import numpy as np

# This method takes all index values out of maximum and minimum range
def index_quantization(channel_coefficients,delta_max,delta_min):
    index_quantization_list = []
    maximum = get_max(channel_coefficients,delta_max)
    minimum = get_min(channel_coefficients,delta_max,delta_min)

    for i in range(0,len(channel_coefficients)):
        if(channel_coefficients[i] > maximum or channel_coefficients[i] < minimum):
            index_quantization_list.append(i)
    
    return index_quantization_list


#this method compute the max of the band guard
def get_max(channel_coefficients,delta_max):
    maximum = np.mean(channel_coefficients) + delta_max
    return maximum

#this method compute the mins of the band guard
def get_min(channel_coefficients,delta_max,delta_min):
    minimum = get_max(channel_coefficients, delta_max) - delta_min
    return minimum          


     