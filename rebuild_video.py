import os
import cv2
import time
import numpy as np
from skimage.metrics import structural_similarity as ssim

# === PATH CONFIGURATION ===
BASE_DIR = r"C:\Users\balav\OneDrive\Pictures\video reconstruction"
FRAMES_PATH = os.path.join(BASE_DIR, "frames_extracted")
OUTPUT_VIDEO = os.path.join(BASE_DIR, "video_reconstructed.mp4")
LOG_FILE = os.path.join(BASE_DIR, "process_log.txt")

os.makedirs(FRAMES_PATH, exist_ok=True)

# === STEP 1: VIDEO TO FRAMES ===
source_video = os.path.join(BASE_DIR, "jumbled_video.mp4")
video_reader = cv2.VideoCapture(source_video)
frame_counter = 0
start_exec = time.time()

while True:
    success, frame = video_reader.read()
    if not success:
        break
    frame_name = os.path.join(FRAMES_PATH, f"img_{frame_counter:04d}.jpg")
    cv2.imwrite(frame_name, frame)
    frame_counter += 1

video_reader.release()
print(f"📸 Total {frame_counter} frames extracted from → {source_video}")

# === STEP 2: FRAME PREPROCESSING ===
frame_files = sorted([f for f in os.listdir(FRAMES_PATH) if f.endswith('.jpg')])
all_frames = [cv2.imread(os.path.join(FRAMES_PATH, f)) for f in frame_files]
gray_resized = [cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), (160, 90)) for f in all_frames]

num_frames = len(all_frames)
print(f"🧩 Frames ready for analysis: {num_frames}")

# === STEP 3: SIMILARITY MATRIX GENERATION ===
similarity_map = np.zeros((num_frames, num_frames), dtype=np.float32)

for i in range(num_frames):
    for j in range(i + 1, num_frames):
        similarity_score = ssim(gray_resized[i], gray_resized[j])
        similarity_map[i, j] = similarity_map[j, i] = similarity_score

# === STEP 4: GREEDY ORDER CONSTRUCTION ===
visited_frames = [False] * num_frames
sequence_order = [0]
visited_frames[0] = True

for _ in range(1, num_frames):
    last_idx = sequence_order[-1]
    possible_scores = similarity_map[last_idx] * np.logical_not(visited_frames)
    next_frame = int(np.argmax(possible_scores))
    visited_frames[next_frame] = True
    sequence_order.append(next_frame)

print("🧠 Frame sequence estimated using SSIM-based greedy traversal.")

# === STEP 5: MOTION CONTINUITY CHECK ===
def avg_sequence_similarity(order, gray_frames):
    values = []
    for i in range(len(order) - 1):
        f1, f2 = order[i], order[i + 1]
        values.append(ssim(gray_frames[f1], gray_frames[f2]))
    return np.mean(values)

forward_score = avg_sequence_similarity(sequence_order, gray_resized)
reverse_score = avg_sequence_similarity(sequence_order[::-1], gray_resized)
print(f"➡️ Forward Smoothness: {forward_score:.4f}")
print(f"⬅️ Reverse Smoothness: {reverse_score:.4f}")

if reverse_score > forward_score:
    print("🔁 Direction adjusted — reverse order produces smoother playback.")
    sequence_order.reverse()
else:
    print("✅ Direction retained — forward playback is smoother.")

# === STEP 6: VIDEO RECONSTRUCTION ===
height, width, _ = all_frames[0].shape
video_writer = cv2.VideoWriter(OUTPUT_VIDEO, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

for idx in sequence_order:
    video_writer.write(all_frames[idx])

video_writer.release()

total_time = time.time() - start_exec
print(f"🎞️ Reconstructed video saved successfully at: {OUTPUT_VIDEO}")
print(f"⏱️ Process completed in: {total_time:.2f} seconds.")

with open(LOG_FILE, "a", encoding="utf-8") as log:
    log.write(f"Runtime: {total_time:.2f} seconds\nProcess completed successfully.\n")
