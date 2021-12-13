from typing import List

import numpy as np
from utils import _flatten


def get_emission_parameters(
    features_encoded: List[List[int]], labels_encoded: List[List[int]]
) -> np.ndarray:
    num_features = max(_flatten(features_encoded)) + 1
    num_labels = max(_flatten(labels_encoded)) + 1

    emission = np.zeros((num_labels, num_features))

    for i, j in zip(labels_encoded, features_encoded):
        for state, observation in zip(i, j):
            emission[state, observation] += 1

    emission_params = emission / emission.sum(axis=0)
    return emission_params
