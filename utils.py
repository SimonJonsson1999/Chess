
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

id_to_class = {v: c for c, v in classes.items()}



ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, 
            "5": 3, "6": 2, "7": 1, "8": 0}
rowsToRanks = {v: k for k, v in ranksToRows.items()}
filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, 
            "e": 4, "f": 5, "g": 6, "h": 7}
colsToFiles = {v: k for k, v in filesToCols.items()}

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

    id_to_class = {v: c for c, v in classes.items()}
    x = torch.randint(0, len(dataset), (1,)).item()
    image = dataset[x][0]
    image = image.to(device)
    plot_image(image.cpu())
    
    with torch.inference_mode():
        logits = model(image.unsqueeze(dim=0))
        pred = torch.argmax(torch.softmax(logits, dim=1), dim=1)
        print(f"model predicted --> {id_to_class[pred.item()]}")
    print(f"label is {dataset[x][1]} ({id_to_class[dataset[x][1].item()]})")