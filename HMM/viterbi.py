import numpy as np

def viterbi_algorithm(word_arr, Transmission, Emission):
    # TODO: PART 2 - Implement this, not sure what parameters you wanna make use of
    # TODO: PART 3 - Viterbi can take another parameters k that outputs the k-th best sequence
    
    """
    Followed pseudocode here
    https://en.wikipedia.org/wiki/Viterbi_algorithm#Pseudocode
    """
    S = list(Transmission.count.keys()) #set of all possible tags remove #START# and #STOP#
    S.remove('#START#')
    S.remove('#END#')
    A = Transmission.vector_proba # A(tag_u_vector,tag_v)
    B = Emission.emission # B(tag_u->word)
    T = len(S) # Total number unique tags
    N = len(word_arr) # Length of sentence make sure no #START# and #STOP#
    
    T1 = np.zeros((T,N)) #probability table of most possible path to node i.e. store scores of each node
    T2 = np.zeros((T,N)) # Table of paths where the ith row stores highest scoring paths to T1[i,j]
    
    #Handle first word and base case at the same time
    for i in range(T):
        T1[i,0] = 1 * Transmission.transmission_proba('#START#',S[i]) * B(S[i],word_arr[0])
        T2[i,0] = 0 #Path for first column is set to 0 same for all
    
    #Note A is vector operation
    # Fill up each column by using previous column
    # j is position of word
    for j in range(1,N):
        # i is position of tag
        #ignore #START# and #END# tag when looping
        for i in range(T):
            tag = S[i]
            #note A(S,tag_u gives a vector)
            T1[i][j] = np.max(T1[:,j-1]*A(S,tag)*B(tag,word_arr[j])) 
            T2[i][j] = np.argmax(T1[:,j-1]*A(S,tag))
    
    #handle last word to #END#
    #no emission of #END# 
    best_row = np.argmax(T1[:,N-1]*A(S,'#END#'))
    ans=[]
    for j in range(1,N):
        index = int(T2[best_row][j])
        ans.append(S[index])
    ans.append(S[best_row])
    
    return ans