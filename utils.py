
#This method compute the similiraty index (SI) for alice and bob
def compute_si(indexes_1,indexes_2):
    if(len(indexes_2)!=0):
        si = len(set(indexes_1).intersection(set(indexes_2)))/len(set(indexes_2))
    
    return si

def find_max_with_list_names(dict_samples_SI):
    results = []
    # Extract the list names and the lists from the dictionary
    names = list(dict_samples_SI.keys())
    lists = list(dict_samples_SI.values())
    
    # Iterate through the corresponding elements of the lists
    for elements in zip(*lists):
        max_value = max(elements)
        max_index = elements.index(max_value)
        # Add the maximum value and the name of the list it came from
        results.append((names[max_index]))
    
    return results