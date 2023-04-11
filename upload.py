from argparse import ArgumentParser
from transformers import AutoTokenizerFast

# Import the model you want to upload or checkpoint class
# This is just a dummy class
from dummy_class import *

def parse_argument():
    parser = ArgumentParser()
    parser.add_argument("--model_type", default="lightning", type=str)
    parser.add_argument("--tokenizer_path", required=True, type=str)
    parser.add_argument("--checkpoint_path", required=True, type=str)
    parser.add_argument("--repo_address", required=True, type=str)
    
    args = parser.parse_args()
    
    return args

def lightning_push(config):
    # Pass the checkpoint path to the method
    model = DummyModelForLightning.load_from_checkpoint(config.checkpoint_path)

    # pytorch lightning model has huggingface model as member variable
    # Pass the huggingface repository address to the method
    model.model.push_to_hub(config.repo_address)

    # Pass the vocab.txt path to the method
    # The path is not the path of the file, but the path of the folder containing vocab.txt
    tokenizer = AutoTokenizerFast.from_pretrained(config.tokenizer_path)

    # Pass the huggingface repository address to the method
    tokenizer.push_to_hub(config.repo_address)


def huggingface_push(config):
    # Pass the checkpoint path to the method
    model = DummyModelForHuggingFace()

    # pytorch lightning model has huggingface model as member variable
    # Pass the huggingface repository address to the method
    model.push_to_hub(config.repo_address)

    # Pass the vocab.txt path to the method
    # The path is not the path of the file, but the path of the folder containing vocab.txt
    tokenizer = AutoTokenizerFast.from_pretrained(config.tokenizer_path)

    # Pass the huggingface repository address to the method
    tokenizer.push_to_hub(config.repo_address)


if __name__ == "__main__":
    print("Model type must be either: lightning or huggingface")
    config = parse_argument()

    if config.model_type == "lightning":
        lightning_push(config)

    elif config.model_type == "huggingface":
        huggingface_push(config)

    else:
        raise ValueError("Wrong model type! Must be either: lightning or huggingface")