import cv2
import os
from tqdm import tqdm

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames: {total_frames}")

    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_dir, f"frame_{idx:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        idx += 1

    cap.release()
    print(f"✅ Extracted {idx} frames to {output_dir}")

if __name__ == "__main__":
    video_path = r"D:\jumbled-reconstruction\data\jumbled_video.mp4"
    output_dir = r"D:\jumbled-reconstruction\data\frames"
extract_frames(video_path, output_dir)
