import torch
from torch import nn
from torchvision import transforms
from torch.utils.data import DataLoader, random_split, TensorDataset
import torchvision.models as models

class Net(nn.Module):
    def __init__(self, n_classes):
        super().__init__()
        self.resnet18 = models.resnet18(pretrained=True)
        self.resnet18.fc = nn.Linear(self.resnet18.fc.in_features, n_classes)
        for param in self.resnet18.layer4.parameters():
            param.requires_grad = True
        for param in self.resnet18.fc.parameters():
            param.requires_grad = True
            
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.resnet18(x)
    
def train_model(model, train_dataloader, val_dataloader, loss_fn, optimizer, epochs, device):
    model.train()  
    for epoch in range(epochs):  
        for images, labels in train_dataloader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = loss_fn(outputs, labels)
            loss.backward()
            optimizer.step()
        train_accuracy = calculate_accuracy(model, val_dataloader, device)
        print(f"Epoch [{epoch+1}/{epochs}], Training Accuracy: {train_accuracy:.2f}%, Loss: {loss.item():.4f}")

def calculate_accuracy(model, dataloader, device):
    model.eval() 
    correct = 0
    total = 0
    
    with torch.no_grad():  
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = (correct / total) * 100
    return accuracy