
# Discard all indexes out of the second interval of quantization
def quantization_by_indexes_alice(channel_coefficients,quantization_intervals):
    quantization_by_indexes=[]
    for i in range(0,len(channel_coefficients)):
        if channel_coefficients[i] >= quantization_intervals[3] or channel_coefficients[i] < quantization_intervals[2]:
            quantization_by_indexes.append(i)
    return quantization_by_indexes


# Discard all indexes out of first second and third interval of quantization
def quantization_by_indexes_bob(channel_coefficients,quantization_intervals):
    quantization_by_indexes=[]

    for i in range(0,len(channel_coefficients)):
        if channel_coefficients[i] >= quantization_intervals[4]:
           quantization_by_indexes.append(i) 
    return quantization_by_indexes