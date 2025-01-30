import tkinter as tk
from PIL import ImageTk, Image
import cv2
import numpy as np
import time

# Function to simulate weed detection using a machine learning model
def detect_weeds(frame):
    # Simulate detection by finding green areas in the image
    blurred = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    weed_locations = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Threshold for considering it as a weed
            x, y, w, h = cv2.boundingRect(contour)
            weed_locations.append((x + w // 2, y + h // 2))  # Center coordinates
    return weed_locations

# Function to simulate robotic arm movement to remove weeds
def remove_weed(weed_location):
    # Simulate arm movement (for demonstration purposes, we'll just print the location)
    print(f"Removing weed at location: {weed_location}")
    time.sleep(1)  # Simulate the time taken to remove the weed

class RobotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Agricultural Robot")
        
        # Canvas to display camera feed
        self.canvas = tk.Canvas(master, width=640, height=480)
        self.canvas.grid(row=0, column=0, columnspan=3)
        
        # Start button
        self.start_button = tk.Button(master, text="Start", command=self.start_detection)
        self.start_button.grid(row=1, column=0)
        
        # Stop button
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_detection)
        self.stop_button.grid(row=1, column=1)
        
        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=1, column=2)
        
        # Camera
        self.cap = cv2.VideoCapture(0)
        self.update()
    
    def update(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.master.after(10, self.update)
    
    def start_detection(self):
        # Placeholder for machine learning model for weed detection
        # For demonstration, we'll just simulate detection using the camera feed
        ret, frame = self.cap.read()
        if ret:
            weed_locations = detect_weeds(frame)
            for weed_location in weed_locations:
                remove_weed(weed_location)
    
    def stop_detection(self):
        # Placeholder for stopping detection
        pass

if __name__ == "__main__":
    root = tk.Tk()
    gui = RobotGUI(root)
    root.mainloop()
