
# Transform number of points (k) in degree of polynomial (k-1)
def transform_in_degree(dictionary):
    new_dictionary = {}
    for key in dictionary:
        new_key = key - 1
        new_dictionary[new_key] = dictionary[key]
    
    return new_dictionary
