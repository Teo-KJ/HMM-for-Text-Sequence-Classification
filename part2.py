from HMM.emission import get_emission_parameters
from HMM.transition import get_transition_parameters
from utils import DATASETS, load_data, encode_token, write_data, remove_features_in_test_and_not_in_training

if __name__ == "__main__":
    for dataset in DATASETS:
        feat_train, label_train = load_data(path=f"{dataset}/train")
        feat_in, _ = load_data(path=f"{dataset}/dev.in")

        feat_train_encoded, feat_map = encode_token(tokens=feat_train)
        label_train_encoded, label_map = encode_token(tokens=label_train)

        emission_params = get_emission_parameters(features_encoded=feat_train_encoded,
                                                  labels_encoded=label_train_encoded)
        transition_params = get_transition_parameters(labels_encoded=label_train_encoded)

        feat_in_cleaned = remove_features_in_test_and_not_in_training(features_test=feat_in,
                                                                      features_training=feat_train)
        """
        # TODO: PART 2 - Call viterbi here to get predicted labels
        """
        labels_in_predicted = [] # update this

        write_data(path=f"{dataset}/dev.p2.out", features_predicted=feat_in, labels_predicted=labels_in_predicted)