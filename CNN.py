import torch
from torch import nn
from torchvision import transforms
from torch.utils.data import DataLoader, random_split, TensorDataset
import torchvision.models as models

class Net(nn.Module):
    def __init__(self, n_classes):
        super().__init__()
        
        # Load the pretrained ResNet-18 model
        self.resnet18 = models.resnet18(pretrained=True)
        
        # Modify the final fully connected layer (classifier) to match n_classes
        self.resnet18.fc = nn.Linear(self.resnet18.fc.in_features, n_classes)
        
        # Fine-tune: Unfreeze the last layer block and the fully connected layer
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

        # After each epoch, calculate and print the training accuracy
        train_accuracy = calculate_accuracy(model, val_dataloader, device)
        print(f"Epoch [{epoch+1}/{epochs}], Training Accuracy: {train_accuracy:.2f}%, Loss: {loss.item():.4f}")

def calculate_accuracy(model, dataloader, device):
    model.eval()  # Set the model to evaluation mode
    correct = 0
    total = 0
    
    with torch.no_grad():  # Turn off gradients to save memory and computation
        for inputs, labels in dataloader:
            # Move data to the device (GPU or CPU)
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Forward pass
            outputs = model(inputs)
            
            # Get the predictions
            _, predicted = torch.max(outputs, 1)
            
            # Update the number of correct predictions
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    
    # Calculate accuracy
    accuracy = (correct / total) * 100
    return accuracy