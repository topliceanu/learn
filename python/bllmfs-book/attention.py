import torch

def softmax_naive(x):
    # You're better off using torch.softmax()
    return torch.exp(x) / torch.exp(x).sum(dim=0)

def context_vecs(inputs):
    # Attention scores are the dot products of the embeddings for every pair of words in the input.    
    attn_scores = inputs @ inputs.T
    # Attention weights are normalised scores using softmax, this makes them into a probability distribution per each column.
    attn_weights = torch.softmax(attn_scores, dim=-1)
    # The context vector is obtained for each word by multiplying with the attention weights 
    return attn_weights @ inputs

inputs = torch.tensor(
    [[0.43, 0.15, 0.89], # Your (x^1)
    [0.55, 0.87, 0.66], # journey (x^2)
    [0.57, 0.85, 0.64], # starts (x^3)
    [0.22, 0.58, 0.33], # with (x^4)
    [0.77, 0.25, 0.10], # one (x^5)
    [0.05, 0.80, 0.55]] # step (x^6)
)

all = context_vecs(inputs)
print(all)
    