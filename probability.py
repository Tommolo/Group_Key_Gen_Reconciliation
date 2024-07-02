

def calculate_probabilities(all_common_values_ab_ba, all_common_values_ba_ae, all_common_values_ba_be):
    # Calculate probabilities: length as key and probability (number of elements/iterations) as value
    prob_intersection_ab_ba = {length: all_common_values_ab_ba.count(length) / len(all_common_values_ab_ba) for length in set(all_common_values_ab_ba)}
    prob_intersection_ba_ae = {length: all_common_values_ba_ae.count(length) / len(all_common_values_ba_ae) for length in set(all_common_values_ba_ae)}
    prob_intersection_ba_be = {length: all_common_values_ba_be.count(length) / len(all_common_values_ba_be) for length in set(all_common_values_ba_be)}

    return {
        "prob_intersection_ab_ba": prob_intersection_ab_ba,
        "prob_intersection_ba_ae": prob_intersection_ba_ae,
        "prob_intersection_ba_be": prob_intersection_ba_be
    }


def sort_probabilities(prob_intersection_ab_ba, prob_intersection_ba_ae, prob_intersection_ba_be):
    # Sort probabilities by length for plotting
    sorted_lengths_intersection_ab_ba = sorted(prob_intersection_ab_ba.keys())
    sorted_probs_intersection_ab_ba = [prob_intersection_ab_ba[length] for length in sorted_lengths_intersection_ab_ba]

    sorted_lengths_intersection_ba_ae = sorted(prob_intersection_ba_ae.keys())
    sorted_probs_intersection_ba_ae = [prob_intersection_ba_ae[length] for length in sorted_lengths_intersection_ba_ae]

    sorted_lengths_intersection_ba_be = sorted(prob_intersection_ba_be.keys())
    sorted_probs_intersection_ba_be = [prob_intersection_ba_be[length] for length in sorted_lengths_intersection_ba_be]

    return {
        "sorted_lengths_intersection_ab_ba": sorted_lengths_intersection_ab_ba,
        "sorted_probs_intersection_ab_ba": sorted_probs_intersection_ab_ba,
        "sorted_lengths_intersection_ba_ae": sorted_lengths_intersection_ba_ae,
        "sorted_probs_intersection_ba_ae": sorted_probs_intersection_ba_ae,
        "sorted_lengths_intersection_ba_be": sorted_lengths_intersection_ba_be,
        "sorted_probs_intersection_ba_be": sorted_probs_intersection_ba_be
        }


#  Create a dictionary common_value:probability
def compute_frequency_and_probability(list):
    prob_dictionary = {}
    length_list = len(list)  

    for value in sorted(list):
        if value not in prob_dictionary:
            frequency = list.count(value) # count number of times this value is in the list
            probability = frequency / length_list 
            prob_dictionary[value] = probability
            
    return prob_dictionary


# We consider the success probability the capability to reconstruct a polynomial of grade k 
def compute_success_probability(dictionary, list):
    new_dictionary = {}
    
    # Sort the keys of the dictionary for safety
    sorted_keys = sorted(dictionary.keys())
    
    for l in list:
        probability_sum = 0
        for key in sorted_keys:
            if l > key:
                probability_sum += dictionary[key]
        new_dictionary[l] = 1 - probability_sum
    
    return new_dictionary