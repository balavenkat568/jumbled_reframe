import numpy as np

def tsp_reorder(similarity):
    n = similarity.shape[0]
    visited = np.zeros(n, dtype=bool)
    order = [0]  # start from first frame
    visited[0] = True

    for _ in range(n - 1):
        last = order[-1]
        sims = similarity[last]
        sims[visited] = -1  # avoid revisiting
        next_idx = np.argmax(sims)
        order.append(next_idx)
        visited[next_idx] = True

    return order

if __name__ == "__main__":
    sim_path = "../data/similarity_matrix.npy"
    order_out = "../data/frame_order_final.npy"

    print("🧩 Loading similarity matrix...")
    similarity = np.load(sim_path)
    print(f"Shape: {similarity.shape}")

    print("🚀 Solving frame order using greedy TSP approach...")
    order = tsp_reorder(similarity)
    np.save(order_out, np.array(order))

    forward_score = np.mean([
        similarity[order[i], order[i+1]]
        for i in range(len(order)-1)
    ])

    print(f"✅ Order saved to {order_out}")
    print(f"📈 Forward continuity score: {forward_score:.4f}")
