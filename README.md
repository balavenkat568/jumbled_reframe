# 🎞️ Video Frame Reconstruction using SSIM (Python)

This project reconstructs a **jumbled or shuffled video** back into its natural, continuous order using **SSIM (Structural Similarity Index)** between frames.

It uses OpenCV and NumPy to extract, analyze, and reorder frames to make the video appear smooth and forward-moving again.

---

## 🧠 Overview

The algorithm works by:
1. Extracting all frames from the input video.
2. Converting frames to grayscale and resizing them for faster comparison.
3. Computing a **similarity matrix** between all pairs of frames using SSIM.
4. Reordering frames using a **greedy traversal** based on visual similarity.
5. Evaluating both forward and reverse playback directions.
6. Outputting the smoother version as the reconstructed video.

---

## 🚀 Example Output

Total 300 frames extracted from → jumbled_video.mp4
Frames ready for analysis: 300
Frame sequence estimated using SSIM-based greedy traversal.
Forward Smoothness: 0.9463
Reverse Smoothness: 0.8034
Direction retained — forward playback is smoother.
Reconstructed video saved successfully at: C:\Users\balav\OneDrive\Pictures\video reconstruction\video_reconstructed.mp4
Process completed in: 285.45 seconds.

yaml
Copy code

---

## 📂 Folder Structure

video reconstruction/
├── jumbled_video.mp4 # Input jumbled video
├── rebuild_video_new.py # Main Python script
├── frames_extracted/ # Folder created to store all frames
│ ├── img_0000.jpg
│ ├── img_0001.jpg
│ └── ...
├── video_reconstructed.mp4 # Final reconstructed video
└── process_log.txt # Execution time and log info

yaml
Copy code

---

## 🧩 Key Functions

### `avg_sequence_similarity(order, gray_frames)`
Calculates average SSIM between consecutive frames in a given order to measure smoothness.

**Parameters**
- `order`: List of frame indices
- `gray_frames`: Grayscale frame list

**Returns**
- Average SSIM value (float)

---

## ⚙️ Requirements

Make sure you have Python 3.10+ installed, then run:

```bash
pip install opencv-python numpy scikit-image
▶️ How to Run
Open VS Code.

Open your folder:

makefile
Copy code
C:\Users\balav\OneDrive\Pictures\video reconstruction
Create or confirm the file rebuild_video_new.py.

Make sure the input video jumbled_video.mp4 is inside the same folder.

Open Terminal in VS Code and run:

bash
Copy code
python rebuild_video_new.py
After running, your reconstructed video will be saved as:

makefile
Copy code
C:\Users\balav\OneDrive\Pictures\video reconstruction\video_reconstructed.mp4
📈 Advantages
✅ Simple and unsupervised — no ML model required
✅ Automatically detects correct playback direction
✅ Works for most short videos (≤10 seconds @ 30fps)
✅ Generates frame-level smoothness statistics

⚠️ Limitations
⚠️ SSIM calculation is computationally expensive for longer videos
⚠️ Does not handle scene cuts or rapid lighting changes well
⚠️ Works best for continuous motion scenes

🧑‍💻 Author
Bala Venkat Kandepalli (balavenkat568)
Project: Jumbled Frame Reconstruction using SSIM-based Frame Ordering
