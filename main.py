from parser import load_data, encode_features, remove_features_in_test_and_not_in_training, decode_enc_features

DATASETS = ["ES", "RU"]

# Part 0
"""
Parse data 
"""


# Part 1
def get_emission_parameters():
    pass


def get_emission_probabilities():
    pass


def simple_sentiment_analysis():
    pass


# Do part 2 and 3 together
# Part 2
def get_transition_parameters():
    pass


def viterbi():
    pass


# Part 3
def find_best_output_sequences():
    pass


if __name__ == "__main__":
    for dataset in DATASETS:
        feat_train, label_train = load_data(path=f"{dataset}/train")
        feat_in, label_in = load_data(path=f"{dataset}/dev.in")
        feat_out, label_out = load_data(path=f"{dataset}/dev.out")

        feat_in = remove_features_in_test_and_not_in_training(features_test=feat_in, features_training=feat_train)
        print(feat_in)

        feat_in_encoded, token_map = encode_features(features=feat_in)

        print(feat_in_encoded)
        print(token_map)

        feat_in_enc_decoded = decode_enc_features(features_encoded=feat_in_encoded, token_map=token_map)
        assert feat_in == feat_in_enc_decoded
