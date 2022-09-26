import torch
import os
from transformers import RobertaConfig, RobertaModel, RobertaTokenizer

#device = torch.device("cuda")

def get_roberta_model():

    # Initializing a RoBERTa configuration
    configuration = RobertaConfig()

    # Initializing a model from the configuration
    Roberta_Model = RobertaModel(configuration).from_pretrained("roberta-base")
    #Roberta_Model.to(device)

    # Accessing the model configuration
    configuration = Roberta_Model.config

    #get the Roberta Tokenizer
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')

    return Roberta_Model, tokenizer, configuration
