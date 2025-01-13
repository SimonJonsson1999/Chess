import cv2
import numpy as np
from PIL import ImageGrab
import torchvision.transforms as transforms

from utils import *
from CNN import *
from main import ChessGame

def load_roi_points(filename="roi_points.txt"):
    points = []
    with open(filename, "r") as file:
        for line in file.readlines():
            x, y = map(int, line.strip().split(","))
            points.append((x, y))
    return points

def capture_roi(points):
    if len(points) != 4:
        print("Error: You must have exactly 4 points to define the ROI.")
        return None

    top_left = points[0]
    bottom_right = points[2]

    screen = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
    

    screen_np = np.array(screen)
    screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

    return screen_bgr

def predict_label(model, image, device, id_to_class):
    """
    Predicts the label of a single image using a trained model.
    
    Args:
        model (torch.nn.Module): The trained model.
        image (torch.Tensor): The input image tensor (shape [3, 85, 85]).
        device (torch.device): The device to run the prediction on.
        id_to_class (dict): A dictionary mapping class indices to class names.
        
    Returns:
        str: The predicted label name.
    """
    # Move the image to the device
    image = image.to(device)
    
    with torch.inference_mode():
        # Add batch dimension and pass through the model
        logits = model(image.unsqueeze(dim=0))  # Shape: [1, n_classes]
        
        # Get predicted class
        pred = torch.argmax(torch.softmax(logits, dim=1), dim=1)  # Shape: [1]
        
    # Return the class name
    return id_to_class[pred.item()]

def compare_boards(initial_board, next_board):
    changes = []  # List to store changes
    
    for i in range(8):  # Loop through rows
        for j in range(8):  # Loop through columns
            if initial_board[i][j] != next_board[i][j]:
                changes.append(((i, j), initial_board[i][j], next_board[i][j]))
    
    return changes

def main():
    points = load_roi_points("roi_points.txt")
    chessboard1 = [[-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],]

    chessboard2 = [[-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],
                  [-1,-1,-1,-1,-1,-1,-1,-1],]
    if not points:
        print("Error: No ROI points found!")
        return
    device = "cuda" if torch.cuda.is_available() else "cpu"
    net = Net(n_classes=7).to(device)
    net.load_state_dict(torch.load("chess_piece_classifier.pth"))
    net.eval()  

    cropped_screenshot = cv2.imread("cropped_screenshot.png")
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((85,85))
    ])
    box_size = cropped_screenshot.shape[0] // 8
    board_image = cropped_screenshot.transpose(2,0,1)
    for i in range(8):
        for j in range(8):
            square = cropped_screenshot[box_size*i:box_size*(i+1), box_size*j:box_size*(j+1)]
            square_tensor = transform(square)
            label = predict_label(net, square_tensor, device, id_to_class)
            chessboard1[i][j] = label
            print(f"Square ({i}, {j}): {label}")





    cropped_screenshot = cv2.imread("second_image.png")
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((85,85))
    ])
    box_size = cropped_screenshot.shape[0] // 8
    board_image = cropped_screenshot.transpose(2,0,1)
    for i in range(8):
        for j in range(8):
            square = cropped_screenshot[box_size*i:box_size*(i+1), box_size*j:box_size*(j+1)]
            square_tensor = transform(square)
            label = predict_label(net, square_tensor, device, id_to_class)
            chessboard2[i][j] = label
            print(f"Square ({i}, {j}): {label}")




    
    changes = compare_boards(chessboard1, chessboard2)
    print(changes)



    
if __name__ == "__main__":
    main()