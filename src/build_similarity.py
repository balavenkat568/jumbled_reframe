import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os

# === Load extracted features ===
features_path = "../data/frame_features.npy"
output_path = "../data/similarity_matrix.npy"

if not os.path.exists(features_path):
    print("❌ Feature file not found. Run feature_extraction.py first.")
    exit()

# Load feature vectors
features = np.load(features_path)
print(f"✅ Loaded features: {features.shape}")

# === Compute similarity matrix ===
print("🧠 Computing cosine similarity between frames...")
similarity_matrix = cosine_similarity(features)

# === Save similarity matrix ===
np.save(output_path, similarity_matrix)
print(f"✅ Saved similarity matrix to {output_path}")
print(f"Matrix shape: {similarity_matrix.shape}")
