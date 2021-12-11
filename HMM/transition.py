from typing import List
from collections import defaultdict

def get_transition_parameters(labels_encoded: List[List[int]]):
    # TODO: PART 2 - Implement this
    
    del labels_encoded[-1] #delete last item from the list
        #print(seq)
    transmissions = defaultdict(int)
    count_u = defaultdict(int)

    for i in range(len(labels_encoded)-1):
        tag_u = labels_encoded[i]
        count_u[tag_u] += 1 # need to count #END# too
        if tag_u == "#END#":
            continue

        #if u is not #END# we count the transmission 
        tag_v = labels_encoded[i+1]

        if (tag_u =="#START#" and tag_v == "#END#"):
            #check for empty blank lines at the end and dont count them
            print('these are blank lines')
            count_u["#START#"] -= 1 #remove additional start
            break
        transmissions[(tag_u,tag_v)] += 1

    return transmissions, count_u