from typing import Dict, List, Optional, Tuple

DATASETS = ["ES", "RU"]

def _flatten(t):
    return [item for sublist in t for item in sublist]


def load_data(path: str) -> Tuple[List[List[str]], List[List[str]]]:
    """
    Load data from path and returns a features list and correspond labels:
    e.g. [['hello', 'world', '.'], ['nice', 'work']], [['B-POSITIVE', 0, 0], [0, 'B-POSITIVE']]
    """
    sequences = []
    with open(path) as f:
        for sentence in f.read().split("\n\n"):
            if not sentence:
                continue
            sequences.append(sentence.split("\n"))
    sequences = [[pair.split() for pair in seq] for seq in sequences]
    features = [[pair[0] for pair in seq] for seq in sequences]
    labels = [[pair[1] if len(pair) > 1 else None for pair in seq] for seq in sequences]
    return features, labels


def write_data(path: str, features_predicted: List[List[str]], labels_predicted: List[List[str]]):
    with open(path, "w") as f:
        for feature, label in zip(features_predicted, labels_predicted):
            for token, l in zip(feature, label):
                print(token, l, file=f)
            print(file=f)


def remove_features_in_test_and_not_in_training(
        features_test: List[List[str]], features_training: List[List[str]]
) -> List[List[str]]:
    """
    Replace characters in test that is not found in training with "#UNK#"
    """
    words_training = set(_flatten(features_training))
    return [
        [x if x in words_training else "#UNK#" for x in feature] for feature in features_test
    ]


def encode_token(
        tokens: List[List[str]], token_map: Optional[Dict[str, int]] = None
) -> Tuple[List[List[int]], Dict[str, int]]:
    if not token_map:
        tokens = set(_flatten(tokens))
        token_map = {token: i for i, token in enumerate(tokens)}
    tokens_encoded = [[token_map[x] for x in token] for token in tokens]
    return tokens_encoded, token_map


def decode_enc_tokens(tokens_encoded: List[List[int]], token_map: Dict[str, int]) -> List[List[str]]:
    reverse_map = {i: t for t, i in token_map.items()}
    features = [[reverse_map[x] for x in token] for token in tokens_encoded]
    return features
