from typing import List
import numpy as np

from utils import _flatten


def get_transition_parameters(labels_encoded: List[List[int]]) -> np.ndarray:
    n_params = max(_flatten(labels_encoded)) + 1
    transition_params = np.zeros((n_params + 1, n_params + 1))
    for label in labels_encoded:
        transition_params[0, label[0]] += 1
        transition_params[label[-1] + 1, n_params] += 1
        for i in range(len(label)):
            transition_params[label[i] + 1, label[i]] += 1

    transition_params = (transition_params.T / transition_params.sum(axis=1)).T
    return transition_params


def get_transition_parameters_deep(labels_encoded: List[List[int]]) -> np.ndarray:
    n_params = max(_flatten(labels_encoded)) + 1
    transition_params = np.zeros((n_params + 1, n_params + 1, n_params + 1))
    for label in labels_encoded:
        transition_params[0, 0, label[0]] += 1
        for i in range(2, len(label)):
            transition_params[label[i - 2], label[i - 1], label[i]] += 1

    transition_params = (transition_params.T / transition_params.sum(axis=1)).T
    return transition_params
