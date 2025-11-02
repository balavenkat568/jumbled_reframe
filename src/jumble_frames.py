import os, random, shutil

input_dir = "../data/frames"
output_dir = "../data/frames_jumbled"

os.makedirs(output_dir, exist_ok=True)

frames = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.png'))]
random.shuffle(frames)

for i, frame in enumerate(frames):
    src = os.path.join(input_dir, frame)
    dst = os.path.join(output_dir, f"{i:03d}.png")
    shutil.copy(src, dst)

print(f"✅ Jumbled {len(frames)} frames into {output_dir}")
