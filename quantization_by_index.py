import numpy as np
from plots import *
from utils import *

def quantization_by_indexes(channel_coefficients,min_index,max_index):
    # Sort and remove duplicates
    channel_coefficients_ordered = sorted(set(channel_coefficients))
    indexes = [] 
    for i in range(len(channel_coefficients)):

        if  channel_coefficients[i]<channel_coefficients_ordered[min_index] or channel_coefficients[i] > channel_coefficients_ordered[max_index] :  # Compare with the m-th element
            indexes.append(i)

    return indexes



def get_dict_alpha_indexes (channel_coefficients):
    alpha = 0
    indexes = []
     # Sort and remove duplicates
    channel_coefficients_ordered = sorted(set(channel_coefficients))
    median_value = np.median(channel_coefficients_ordered)

    median_index = np.argmin(np.abs(np.array(channel_coefficients_ordered) - median_value))
    min_index = median_index
    max_index = median_index
    
    dict_alpha_indexes={}

    while min_index>=0 and max_index<len(channel_coefficients_ordered):
        indexes = quantization_by_indexes(channel_coefficients, min_index, max_index)
        alpha = (len(channel_coefficients) - len(indexes))/len(channel_coefficients)
        alpha=np.round(1-alpha,1)
   
        #<alpha,indexes>
        if(alpha!=0.0 and alpha!=1.0):
            dict_alpha_indexes[alpha]=indexes

        min_index -= 1
        max_index += 1


    return dict_alpha_indexes



    
   
def get_dict_alphas_SI(dict_alpha_indexes_1,dict_alpha_indexes_2):
    dict_SI_alphas ={}
    for alpha_1 in dict_alpha_indexes_1:
        for alpha_2 in dict_alpha_indexes_2:
            dict_SI_alphas[(alpha_1,alpha_2)] = np.round(compute_si(dict_alpha_indexes_1.get(alpha_1),dict_alpha_indexes_2.get(alpha_2)),2)
    return dict_SI_alphas



                    


def get_dict_alpha_SIs (dict_alpha_SIs,dict_alpha_SI):
    
    for alpha in dict_alpha_SI.keys():

        if alpha in dict_alpha_SIs and isinstance(dict_alpha_SIs[alpha], list):
            dict_alpha_SIs.get(alpha).append(dict_alpha_SI.get(alpha))
        else : 
            SI_list = []
            SI_list.append(dict_alpha_SI.get(alpha))
            dict_alpha_SIs[alpha]=SI_list


    return dict_alpha_SI