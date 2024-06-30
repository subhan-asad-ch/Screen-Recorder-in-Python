import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Get screen width and height
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)
fourcc = cv2.VideoWriter_fourcc("XVID")
output = cv2.VideoWriter('output.mp4', fourcc, 60.0, (1280, 720))

# Get the duration for recording
now_start_time = time.time()
duration = int(input("Enter the Duration to Record in Seconds: "))
end_time = now_start_time + duration

# Recording loop
while True:
    # Capture the screen
    image = pyautogui.screenshot()
    frame = np.array(image)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    output.write(frame)

    # Break the loop if the recording time is over
    ctime = time.time()
    if ctime >= end_time:
        break

# Release the VideoWriter object
output.release()
print("Screen Recording has Ended")
