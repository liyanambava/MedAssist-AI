import cv2
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    tensor = transform(image).unsqueeze(0)
    return tensor


def extract_visual_features(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # --- Redness ---
    r, g, b = cv2.split(img_rgb)
    redness_score = np.mean(r - (g + b) / 2)

    # --- Swelling / Brightness ---
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness_score = np.mean(gray)

    # --- Irregularity (edge density) ---
    edges = cv2.Canny(gray, 100, 200)
    irregularity_score = np.sum(edges) / edges.size

    return {
        "redness": round(float(redness_score), 2),
        "brightness": round(float(brightness_score), 2),
        "irregularity": round(float(irregularity_score), 4)
    }
