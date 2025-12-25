"""
extract_frames.py

This script extracts frames from a laparoscopic surgery video at fixed intervals.
The extracted frames are used for dataset creation and annotation in Roboflow.
"""


import cv2
import os

# ---- File path of your video ----
video_path = "input_laparoscopy.mp4" # Replace with your video file path

# ---- Folder to save frames ----
output_folder = "frames2"
os.makedirs(output_folder, exist_ok=True)

# ---- Open the video ----
video = cv2.VideoCapture(video_path)

# ---- Choose how many frames per second to save ----
fps_to_capture = 2  # extract 2 frames per second

# ---- Get actual FPS of the video ----
video_fps = video.get(cv2.CAP_PROP_FPS)
frame_interval = int(video_fps // fps_to_capture)

count = 0
saved = 0

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Save every Nth frame
    if count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{saved:05d}.jpg")
        cv2.imwrite(filename, frame)
        saved += 1

    count += 1

video.release()
print(f"Saved {saved} frames in folder '{output_folder}'")
