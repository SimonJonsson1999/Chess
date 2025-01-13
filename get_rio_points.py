import cv2
import numpy as np
from PIL import ImageGrab

# Global variables to store points
points = []

# Mouse callback function
def select_points(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN: 
        points.append((x, y))
        print(f"Point {len(points)}: {x}, {y}")
        if len(points) == 4:  
            print("Selected 4 points:", points)

def main():
    global points

    
    screen = ImageGrab.grab()
    frame = np.array(screen)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

   
    cv2.namedWindow("Select Region of Interest")
    cv2.setMouseCallback("Select Region of Interest", select_points)

    print("Click on 4 corners of the region of interest (top-left, top-right, bottom-right, bottom-left).")
    
    while True:
       
        display_frame = frame.copy()

       
        for idx, point in enumerate(points):
            cv2.circle(display_frame, point, 5, (0, 0, 255), -1)  
            cv2.putText(display_frame, f"{idx+1}", point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow("Select Region of Interest", display_frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q') or len(points) == 4:
            break

    cv2.destroyAllWindows()
    with open("roi_points.txt", "w") as f:
        for point in points:
            f.write(f"{point[0]},{point[1]}\n")
    
    print("Points saved to roi_points.txt. You can now use these coordinates.")

if __name__ == "__main__":
    main()
