import heapq
from typing import List, Tuple

import numpy as np


def viterbi_algorithm(
    features: List[int],
    transition_params: np.ndarray,
    emission_params: np.ndarray,
    k: int = 1,
) -> List[Tuple[int]]:
    # TODO: PART 2 - Implement this, not sure what parameters you wanna make use of
    # TODO: PART 3 - Viterbi can take another parameters k that outputs the k-th best sequence

    """
    Followed pseudocode here
    https://en.wikipedia.org/wiki/Viterbi_algorithm#Pseudocode
    """
    transition_params_log = np.log(transition_params)
    transition_params_log[~np.isfinite(transition_params_log)] = -1
    transition_params_log = transition_params_log.tolist()
    emission_params_log = np.log(emission_params)
    emission_params_log[~np.isfinite(emission_params_log)] = -1

    number_states = len(transition_params_log) - 1
    number_observations = len(features)
    states = list(range(number_states))

    out = [[[] for _ in states] for _ in range(number_observations)]

    start = transition_params_log.pop(0)

    for s in states:
        out[0][s].append(
            (
                start[s] + emission_params_log[s, features[0]],
                tuple(),
            )
        )

    # Handle first word and base case at the same time
    for i in range(1, number_observations):
        for s in states:
            h = []
            for prev_state, prev_state_scores in enumerate(out[i - 1]):
                for j, entry in enumerate(prev_state_scores):
                    prev_score, prev_state_path = entry
                    score = (
                        prev_score
                        + transition_params_log[prev_state][s]
                        + emission_params_log[s, features[i]]
                    )
                    h.append((score, tuple(prev_state_path) + (prev_state,)))

            # Update this
            h.sort(reverse=True)
            out[i][s] = h[:k]

    opt = []
    for last_state, entries in enumerate(out[-1]):
        for e in entries:
            heapq.heappush(opt, [e, last_state])

    out = [
        tuple(path) + (last_state,)
        for (score, path), last_state in heapq.nlargest(k, opt)
    ]
    return out
