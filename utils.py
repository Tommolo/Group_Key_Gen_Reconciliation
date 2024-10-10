
#This method compute the similiraty index (SI) for alice and bob
def compute_si(indexes_1,indexes_2):
    if(len(indexes_2)!=0):
        si = len(set(indexes_1).intersection(set(indexes_2)))/len(set(indexes_2))
    
    return si
