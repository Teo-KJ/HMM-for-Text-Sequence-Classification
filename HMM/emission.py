from typing import List
import numpy as np
from utils import *

def get_emission_parameters(features_encoded: List[List[int]], labels_encoded: List[List[int]]) -> List[List[int]]:
    # x - observation, y - states
    # b(x) = count(y->x)/count(y)
    # TODO: PART 1 - Implement this
    
    numObservations = max(_flatten(features_encoded))
    numOfStates = max(_flatten(labels_encoded))

    emission = np.zeros((numOfStates, numObservations))

    for i, j in zip(numOfStates, numObservations):
        for s, o in zip(i, j):
            emission[s, o] += 1

    emission_params = emission / emission.sum(axis=0)
    return emission_params