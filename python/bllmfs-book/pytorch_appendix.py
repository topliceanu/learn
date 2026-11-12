import torch
import torch.nn.functional as F
from torch.autograd import grad
from torch.utils.data import Dataset, DataLoader

# Hardware support

print("Version: ", torch.__version__)
print("CUDA available: ", torch.cuda.is_available())
print("MPS available: ", torch.backends.mps.is_available())

# Gradients and back-propagation

y = torch.tensor([1.0])
x1 = torch.tensor([1.1])
w1 = torch.tensor([2.2], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)

z = x1 * w1 + b
a = torch.sigmoid(z)
loss = F.binary_cross_entropy(a, y)
print("Loss= ", loss)

grad_loss_w1 = grad(loss, w1, retain_graph=True)
grad_loss_b = grad(loss, b, retain_graph=True)

print("grad_loss_w1= ", grad_loss_w1)
print("grad_loss_b= ", grad_loss_b)

# Neural networks

class MultiLayerPerceptronWith2HiddenLayers(torch.nn.Module):
    # This is a 2 hidden layer perceptron: input (num_inputs) > first hidden layer (30) > second hidden layer (20) -> output (num_outputs)
    def __init__(self, num_inputs, num_outputs):
        super().__init__()
        self.layers = torch.nn.Sequential(
            # 1st layer
            torch.nn.Linear(num_inputs, 30),
            torch.nn.ReLU(),
            # 2nd layer
            torch.nn.Linear(30, 20),
            torch.nn.ReLU(),
            # output
            torch.nn.Linear(20, num_outputs),
        )
    
    def forward(self, x):
        logits = self.layers(x)
        return logits # output of the last layer

model = MultiLayerPerceptronWith2HiddenLayers(50, 3)
num_params = sum([p.numel() for p in model.parameters() if p.requires_grad])
print("Trainable parameters: ", num_params)

torch.manual_seed(123)
X = torch.rand((1, 50))
with torch.no_grad():
    out = model(X)
    print("Output= ", out)

# Data loaders 

X_train = torch.tensor([
    [-1.2, 3.1],
    [-0.9, 2.9],
    [-0.5, 2.6],
    [2.3, -1.1],
    [2.7, -1.5]
])
y_train = torch.tensor([0, 0, 0, 1, 1])
X_test = torch.tensor([
    [-0.8, 2.8],
    [2.6, -1.6],
])
y_test = torch.tensor([0, 1])

class ToyDataset(Dataset):
    def __init__(self, X, y):
        self.features = X
        self.labels = y

    def __getitem__(self, index):
        one_x = self.features[index]
        one_y = self.labels[index]
        return one_x, one_y

    def __len__(self):
        return self.labels.shape[0]
        
def compute_accuracy(model, dataloader):
    model = model.eval()
    correct = 0.0
    total_examples = 0

    for idx, (features, labels) in enumerate(dataloader):
        with torch.no_grad():
            logits = model(features)
        predictions = torch.argmax(logits, dim=1)
        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)
    return (correct / total_examples).item()

train_ds = ToyDataset(X_train, y_train)
test_ds = ToyDataset(X_test, y_test)

train_loader = DataLoader(dataset=train_ds, batch_size=2, shuffle=True, num_workers=0, drop_last=True)
test_loader = DataLoader(dataset=test_ds, batch_size=2, shuffle=False, num_workers=0)

new_model = MultiLayerPerceptronWith2HiddenLayers(num_inputs=2, num_outputs=2)
optimizer = torch.optim.SGD(new_model.parameters(), lr=0.5) # Optimizer needs to know the parameters that need to be optimised.
print("New model optimisable parameters: ", sum([p.numel() for p in new_model.parameters() if p.requires_grad]))
num_epochs = 3 
for epoch in range(num_epochs):
    new_model.train()

    for batch_id, (features, labels) in enumerate(train_loader):
        logits = new_model(features)
        loss = F.cross_entropy(logits, labels)
        optimizer.zero_grad() # prevent unintended gradient accumulation.
        loss.backward()
        optimizer.step() # update model parameters from the gradients.

        ### LOGGING
        print(f"Epoch: {epoch+1:03d}/{num_epochs:03d}"
        f" | Batch {batch_id:03d}/{len(train_loader):03d}"
        f" | Train Loss: {loss:.2f}") 

    print("Accuracy: ", compute_accuracy(new_model, train_loader))

