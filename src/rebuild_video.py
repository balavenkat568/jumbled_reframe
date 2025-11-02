import cv2
import numpy as np
import os

if __name__ == "__main__":
    frames_dir = "../data/frames_jumbled"
    order_path = "../data/frame_order_final.npy"
    output_path = "../output/reconstructed_video.mp4"
    fps = 30  # 10 seconds * 30 fps = 300 frames

    print("🎞️ Loading frame order...")
    order = np.load(order_path)
    print(f"Total frames in order: {len(order)}")

    # Collect frame paths
    frame_files = sorted(os.listdir(frames_dir))
    frame_files = [f for f in frame_files if f.endswith(".jpg") or f.endswith(".png")]

    # Use first frame to get resolution
    first_frame = cv2.imread(os.path.join(frames_dir, frame_files[0]))
    height, width, _ = first_frame.shape

    print(f"🛠️ Reconstructing video ({width}x{height}) at {fps} fps...")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for idx in order:
        frame_path = os.path.join(frames_dir, frame_files[idx])
        frame = cv2.imread(frame_path)
        out.write(frame)

    out.release()
    print(f"✅ Reconstructed video saved at: {output_path}")
