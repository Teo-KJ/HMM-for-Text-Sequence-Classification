from tqdm import tqdm

from HMM.emission import get_emission_parameters
from HMM.transition import get_transition_parameters_deep
from HMM.viterbi import modified_viterbi_algorithm
from utils import (
    DATASETS,
    load_data,
    encode_token,
    write_data,
    remove_features_in_test_and_not_in_training,
    decode_enc_tokens,
)

if __name__ == "__main__":
    for dataset in DATASETS:
        for version in ["dev", "test"]:
            feat_train, label_train = load_data(path=f"{dataset}/train")
            feat_in, _ = load_data(path=f"{dataset}/{version}.in")

            feat_train_encoded, feat_map = encode_token(tokens=feat_train)
            label_train_encoded, label_map = encode_token(tokens=label_train)

            emission_params = get_emission_parameters(
                features_encoded=feat_train_encoded, labels_encoded=label_train_encoded
            )

            transition_params = get_transition_parameters_deep(
                labels_encoded=label_train_encoded
            )  # This is a modified transition parameters where we retrieve A->B->C instead of A->B

            feat_in_cleaned = remove_features_in_test_and_not_in_training(
                features_test=feat_in, features_training=feat_train
            )
            feat_in_encoded, _ = encode_token(
                tokens=feat_in_cleaned, token_map=feat_map
            )

            # This is a modified vertibi where we take into account a transition parameter containing a subsequence of 3
            # instead of 2
            labels_in_predicted = [
                modified_viterbi_algorithm(feat, transition_params, emission_params)[-1]
                for feat in tqdm(feat_in_encoded)
            ]

            labels_in_predicted = decode_enc_tokens(
                tokens_encoded=labels_in_predicted, token_map=label_map
            )

            write_data(
                path=f"{dataset}/{version}.p4.out",
                features_predicted=feat_in,
                labels_predicted=labels_in_predicted,
            )
