import cv2
import numpy as np
from PIL import ImageGrab
import torchvision.transforms as transforms
import torch
from utils import *
from CNN import *

class ChessBoardTracker:
    def __init__(self, roi_filename="roi_points.txt", model_path="chess_piece_classifier.pth", device=None):
        self.roi_filename = roi_filename
        self.model_path = model_path
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        
        self.net = Net(n_classes=7).to(self.device)
        self.net.load_state_dict(torch.load(self.model_path))
        self.net.eval()

        self.chessboard_current = [[-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1]]

        self.chessboard_next = [[-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1,-1,-1,-1]]

    def load_roi_points(self):
        points = []
        try:
            with open(self.roi_filename, "r") as file:
                for line in file.readlines():
                    x, y = map(int, line.strip().split(","))
                    points.append((x, y))
        except FileNotFoundError:
            print(f"Error: {self.roi_filename} not found.")
            return None
        return points

    def capture_roi(self, points):
        if len(points) != 4:
            print("Error: You must have exactly 4 points to define the ROI.")
            return None

        top_left = points[0]
        bottom_right = points[2]

        screen = ImageGrab.grab(bbox=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

        return screen_bgr

    def predict_label(self, image, id_to_class):
        """
        Predicts the label of a single image using a trained model.
        
        Args:
            image (torch.Tensor): The input image tensor (shape [3, 85, 85]).
            id_to_class (dict): A dictionary mapping class indices to class names.
            
        Returns:
            str: The predicted label name.
        """
        image = image.to(self.device)

        with torch.inference_mode():
            logits = self.net(image.unsqueeze(dim=0))
            pred = torch.argmax(torch.softmax(logits, dim=1), dim=1)

        return id_to_class[pred.item()]

    def compare_boards(self, initial_board, next_board):
        changes = []
        startpos = None
        endpos = None
        for i in range(8):
            for j in range(8):
                if initial_board[i][j] != next_board[i][j]:
                    if next_board[i][j] == 'empty':
                        startpos = f"{colsToFiles[j]}{int(rowsToRanks[i])}"
                    else:
                        endpos = f"{colsToFiles[j]}{int(rowsToRanks[i])}"
                    changes.append(((i, j), initial_board[i][j], next_board[i][j]))
        return changes, f"{startpos}{endpos}"

    def process_board(self, image):
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((85, 85))
        ])
        box_size = image.shape[0] // 8
        board_image = image.transpose(2, 0, 1)
        
        board = [[None] * 8 for _ in range(8)]

        for i in range(8):
            for j in range(8):
                square = image[box_size * i: box_size * (i + 1), box_size * j: box_size * (j + 1)]
                # cv2.imshow("test", square)
                # cv2.waitKey(0)
                square_tensor = transform(square)
                label = self.predict_label(square_tensor, id_to_class)
                board[i][j] = label
                # print(label)
        return board


    def convert_board(self, board):
        int_board = [[-1 for _ in range(8)] for _ in range(8)]
        
        for i in range(8):
            for j in range(8):
                piece = board[i][j]
                int_board[i][j] = piece.type.lower()
        return int_board
    
    def update_board(self, board):
        int_board = self.convert_board(board)
        self.chessboard_current = int_board


    def get_move(self):
        points = self.load_roi_points()
        next_board_image = self.capture_roi(points)
        self.chessboard_next = self.process_board(next_board_image)
        changes, move = self.compare_boards(self.chessboard_current, self.chessboard_next)
        if len(changes) != 2:
            print(f"Incorrect amount of changes detected")
        else:
            return move


    def test(self):
        points = self.load_roi_points()
        if not points:
            print("Error: No ROI points found!")
            return
        self.chessboard_current = self.process_board("first_image.png")
        self.chessboard_next = self.process_board("second_image.png")

        changes, move = self.compare_boards(self.chessboard_current, self.chessboard_next)
        
        if len(changes) == 2:
            print(move)
        else:
            print(f"Incorrect amount of changes detected")

if __name__ == "__main__":
    tracker = ChessBoardTracker()
    tracker.test()
