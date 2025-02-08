import cv2
import os

# Define the folder where images will be saved
save_folder = "PhotoBoothApp"
os.makedirs(save_folder,exist_ok=True)

# Initialize the image counter
counter = 1

# Open the default webcam
webcam = cv2.VideoCapture(0)

# Check if the webcam is successfully opened
if not webcam.isOpened():
    print("No webcam")
    exit()

# Start the video capture loop
while(True):
    ret, frame = webcam.read()
    
    if frame is None: break
    
    cv2.imshow("WebCam", frame)
    
    # Wait for user input and get the key press
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('s'):
        image = f'{save_folder}/image{counter}.jpg'
        cv2.imwrite(image, frame)
        counter += 1
    
    elif key == ord('q'):
        break
    
webcam.release()
cv2.destroyAllWindows()