import os
import cv2
import numpy as np
from tqdm import tqdm
import torch
import torchvision.models as models
import torchvision.transforms as transforms

def extract_features(frames_dir, output_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    model = models.resnet18(pretrained=True)
    model = torch.nn.Sequential(*list(model.children())[:-1])  # remove classification layer
    model.to(device)
    model.eval()

    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    features = []
    frame_files = sorted(os.listdir(frames_dir))

    for f in tqdm(frame_files, desc="Extracting features"):
        path = os.path.join(frames_dir, f)
        img = cv2.imread(path)
        if img is None:
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        tensor = transform(img).unsqueeze(0).to(device)
        with torch.no_grad():
            feat = model(tensor).cpu().numpy().flatten()
        features.append(feat)

    features = np.array(features)
    np.save(output_path, features)
    print(f"✅ Saved feature vectors to {output_path}")

if __name__ == "__main__":
    extract_features("../data/frames_jumbled", "../data/frame_features.npy")
