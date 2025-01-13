
import matplotlib.pyplot as plt
import PIL
import torch

classes = {
    "bishop": 0,
    "empty": 1,
    "king": 2,
    "knight": 3,
    "pawn": 4,
    "queen": 5,
    "rook": 6, 
}

# Reverse the classes dictionary to create the id_to_class dictionary
id_to_class = {v: c for c, v in classes.items()}



    

def image_to_tensor(image_path, converter):
    image = PIL.Image.open(image_path)
    image_tensor = converter(image)
    return image_tensor

def plot_image(tensor):
    plt.imshow(tensor.permute(1, 2, 0))


def model_pred(model, dataset, device):
    classes = {
    "bishop": 0,
    "empty": 1,
    "king": 2,
    "knight": 3,
    "pawn": 4,
    "queen": 5,
    "rook": 6, 
    }

    # Reverse the classes dictionary to create the id_to_class dictionary
    id_to_class = {v: c for c, v in classes.items()}
    x = torch.randint(0, len(dataset), (1,)).item()
    image = dataset[x][0]
    image = image.to(device)
    plot_image(image.cpu())
    
    with torch.inference_mode():
        logits = model(image.unsqueeze(dim=0)) # inputs must be batched
        pred = torch.argmax(torch.softmax(logits, dim=1), dim=1)
        print(f"model predicted --> {id_to_class[pred.item()]}")
    print(f"label is {dataset[x][1]} ({id_to_class[dataset[x][1].item()]})")