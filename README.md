# 🧠 SSIM-Based Video Frame Reconstruction

## 🐍 Command to Run
```bash
python rebuild_video.py
```

## 🧩 Example Output
```
Extracted 300 frames from jumbled_video.mp4
Loaded 300 frames for reconstruction.
Frame order estimated using SSIM similarity.
Smoothness (forward): 0.9471, Smoothness (reverse): 0.8024
✅ Keeping forward order — smoother sequence confirmed.
🎬 Reconstructed video saved to: C:\Users\balav\OneDrive\Pictures\video reconstruction\reconstructed_forward.mp4
🕒 Total time: 320.45s
```

## 📦 Dependencies
- Python 3.x
- NumPy
- OpenCV
- scikit-image

### Install requirements:
```bash
pip install numpy opencv-python scikit-image tqdm
```

## 📂 Folder Structure
```
video reconstruction/
├── jumbled_video.mp4
├── rebuild_video.py
├── frames/
│   ├── frame_0000.jpg
│   ├── frame_0001.jpg
│   └── ...
├── reconstructed_forward.mp4
└── execution_time_log.txt
```

## 🧩 Key Function: SSIM_Reconstruction()

**Input:**
- A shuffled input video file (`jumbled_video.mp4`)

**Output:**
- Reconstructed video with natural forward motion (`reconstructed_forward.mp4`)
- Execution time log (`execution_time_log.txt`)

## ⚙️ Logic Overview
1. **Frame Extraction**  
   The video is decomposed into individual frames and saved as images.

2. **Preprocessing**  
   Frames are converted to grayscale and downsampled to smaller resolution (160×90) for faster comparison.

3. **SSIM Matrix Computation**  
   For every frame pair `(i, j)`, a **Structural Similarity (SSIM)** score is calculated.  
   This builds an `N × N` matrix representing how visually similar each frame is to the others.

4. **Frame Ordering (Greedy Traversal)**  
   Start from frame `0`. Repeatedly select the **most similar unvisited frame** to the current one.  
   Continue until all frames are ordered.

5. **Smoothness Validation**  
   The average SSIM between consecutive frames is computed in both directions (forward & reverse).  
   The smoother direction is automatically chosen for final reconstruction.

6. **Video Reconstruction**  
   Frames are written to a new `.mp4` file following the computed order.  
   Total execution time is logged.

## 📈 Advantages
✅ Produces a **natural, forward-flowing video**  
✅ Works without deep learning — purely similarity-based  
✅ Automatically detects and fixes reversed sequences  
✅ Easy to run on any machine with Python and OpenCV  

## ⚠️ Limitations
- SSIM comparison is **computationally expensive** for large videos (O(N²)).  
- Works best for **short clips (≤10s @ 30fps)** with consistent lighting and motion.  
- Does not handle scene cuts or abrupt transitions.

## ✨ Author
**balavenkat568 (Bala Venkat Kandepalli)**  
_Project: Jumbled Frame Reconstruction using SSIM Similarity_
