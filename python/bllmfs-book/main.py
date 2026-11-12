import torch
import urllib.request

from tokenizer import tokenizer_v3 as v3
from dataset import create_dataloader_v1

file_path = "the-verdict.txt"

## Download "The verdict" by Edith Wharton
#url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")
#urllib.request.urlretrieve(url, file_path)

# Load it in memory
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of characters: ", len(raw_text))

## Split the text into tokens (words and punctuation; whitespace is ignored).
#preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
#preprocessed = [item.strip() for item in preprocessed if item.strip()]
#print("Total number of words and punctuation: ", len(preprocessed))

## Build a vocabulary; assign each token an ID
#all_words = sorted(set(preprocessed))
#all_tokens.extend([EOT, UNK]) # Add a token to separate different input texts and a token for unknown words.
#vocab_size = len(all_words)
#print("Size of the vocabulary: ", vocab_size)
#vocab = {token: id for id, token in enumerate(all_words)}

## Tokenize the input text, ie. convert The verdict into ids.
#tokenizer = SimpleTokenizerV1(vocab)
#encoded = tokenizer.encode(raw_text)

## Using tiktoken to tokenize the input
#encoded = v3.encode(raw_text, allowed_special={EOT})
#print("Size of encoded text: ", len(encoded))

#dataloader = create_dataloader_v1(raw_text, v3, batch_size=8, max_length=4, stride=4, shuffle=False)
#data_iter = iter(dataloader)
#inputs, targets = next(data_iter)
#print("Inputs:\n", inputs)
#print("\nTargets:\n", targets)

vocab_size = 50257 # Q: How to find the number of symbols in tiktoken?
output_dim = 256 # size of the embeddings.
token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)

max_length = 4
dataloader = create_dataloader_v1(raw_text, tokenizer=v3, batch_size=8, max_length=max_length, stride=max_length, shuffle=False)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)
print("Token IDs:\n", inputs)
print("\nInputs shape:\n", inputs.shape)

token_embeddings = token_embedding_layer(inputs)
print("Token embeddings shape ", token_embeddings.shape)

# Compute absolute positioning embeddings 
context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)
pos_embeddings = pos_embedding_layer(torch.arange(context_length))
print("Positional embeddings shape ", pos_embeddings.shape)

# Input embeddings are the token embeddings and the positional embeddings.
input_embeddings = token_embeddings + pos_embeddings
print("Input embeddings shape ", input_embeddings.shape)