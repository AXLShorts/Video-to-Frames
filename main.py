import cv2
import os

def extract_frames(video_path, output_folder, frames_per_second=0):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames: {total_frames}")
    fps = cap.get(cv2.CAP_PROP_FPS)
    if frames_per_second == 0:
        interval = 1
    else:
        interval = int(round(fps / frames_per_second))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % interval == 0:
            frame_name = f"frame_{frame_count:05d}.jpg"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
        frame_count += 1
    cap.release()

video_path = "./test.mp4"
output_folder = "output_frames"
frames_per_second = 5  # Set to 0 for all frames
extract_frames(video_path, output_folder, frames_per_second)