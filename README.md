🧩 README.md
# Jumbled Reframe Ordering using Greedy TSP

This project reorders shuffled video frames (or image sequences) based on their pairwise similarity matrix.  
It uses a **greedy Traveling Salesman Problem (TSP)** approach to determine the most continuous order of frames.

---

## 📘 Algorithm Overview

The program loads a precomputed similarity matrix between frames — where each value `similarity[i][j]` represents how similar frame *i* is to frame *j*.

It then constructs a path (ordering of frames) such that each next frame is the **most similar** to the current frame, minimizing discontinuities.

---

## ⚙️ How It Works

1. **Input:**  
   A NumPy file `similarity_matrix.npy` containing an NxN similarity matrix.

2. **Algorithm Steps:**
   - Start from the first frame (index `0`).
   - At each step, find the *unvisited* frame with the highest similarity to the current frame.
   - Append that frame to the sequence.
   - Repeat until all frames are visited.
   - Save the resulting order to `frame_order_final.npy`.

3. **Output:**  
   - `frame_order_final.npy`: an array of frame indices representing the reconstructed order.
   - A “forward continuity score” indicating how smooth the ordering is.

---

## 🧠 Example Command

```bash
python c594bf17-5ffe-490f-84bb-6621af98c518.py


Example output:

🧩 Loading similarity matrix...
Shape: (120, 120)
🚀 Solving frame order using greedy TSP approach...
✅ Order saved to ../data/frame_order_final.npy
📈 Forward continuity score: 0.9432

📦 Dependencies

Python 3.x

NumPy

Install requirements:

pip install numpy

📂 Folder Structure
project/
├── src/
│   └── c594bf17-5ffe-490f-84bb-6621af98c518.py
├── data/
│   ├── similarity_matrix.npy
│   └── frame_order_final.npy

🧩 Key Function: tsp_reorder(similarity)
Input:

similarity: A square NumPy array (N, N) of similarity scores.

Output:

A list of frame indices representing the optimal ordering.

Logic:

Mark all frames as unvisited.

Start at frame 0.

Repeatedly select the unvisited frame with the highest similarity to the last visited one.

Continue until all frames are visited.

📈 Advantages

Simple and fast greedy solution for frame sequencing.

Works well when similarity matrix is well-structured.

Useful for unsupervised video reconstruction or temporal ordering tasks.

⚠️ Limitations

Greedy method may not find the optimal TSP path.

Works best when similarity scores strongly reflect sequential relationships.

✨ Author

balavenkat568 (Bala Venkat Kandepalli)
