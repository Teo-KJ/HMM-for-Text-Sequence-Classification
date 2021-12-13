import numpy as np
from tqdm import tqdm

from HMM.emission import get_emission_parameters
from utils import load_data, encode_token, remove_features_in_test_and_not_in_training, decode_enc_tokens, write_data, \
    DATASETS

if __name__ == "__main__":
    for dataset in DATASETS:

        # Data reading and processing
        feat_train, label_train = load_data(path=f"{dataset}/train")
        feat_in, _ = load_data(path=f"{dataset}/dev.in")

        feat_train_encoded, feat_map = encode_token(tokens=feat_train)
        label_train_encoded, label_map = encode_token(tokens=label_train)

        # Model training
        params = get_emission_parameters(features_encoded=feat_train_encoded, labels_encoded=label_train_encoded)

        feat_in_cleaned = remove_features_in_test_and_not_in_training(features_test=feat_in,
                                                                      features_training=feat_train)
        feat_in_encoded, _ = encode_token(tokens=feat_in_cleaned, token_map=feat_map)
        
        # Make predictions
        labels_in_encoded_predicted = [
            np.argmax(params[:, feat], axis=0) for feat in tqdm(feat_in_encoded)
        ]

        labels_in_predicted = decode_enc_tokens(tokens_encoded=labels_in_encoded_predicted, token_map=label_map)

        # update the path for this
        write_data(path=f"{dataset}/dev.p1.out", features_predicted=feat_in, labels_predicted=labels_in_predicted)
