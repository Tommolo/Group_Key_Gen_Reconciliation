
#This method compute the similiraty index (SI) for alice and bob
def compute_si_ab(indexes_ba,indexes_ab,SI_list_ab,set_ab_length):


    if(len(indexes_ab)!=0):
        SI_ab = len(set(indexes_ba).intersection(set(indexes_ab)))/len(set(indexes_ab))
        SI_list_ab.append(SI_ab)
        if(SI_ab==1):
             set_ab_length.append(len(set(indexes_ab)))
        
        return SI_ab

    
#This method compute the similiraty index (SI) for bob and eve
def compute_si_be(indexes_be,indexes_ba,SI_list_be):

    if(len(indexes_be)!=0):
        SI_be = len(set(indexes_ba).intersection(set(indexes_be)))/len(set(indexes_be))
        SI_list_be.append(SI_be)

    return SI_be
