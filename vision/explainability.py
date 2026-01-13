import torch
import numpy as np
import cv2

def generate_heatmap(model, image_tensor):
    image_tensor.requires_grad = True
    output = model(image_tensor)
    score = output.max()
    score.backward()

    gradients = image_tensor.grad[0].mean(dim=0).detach().numpy()
    heatmap = np.maximum(gradients, 0)
    heatmap /= heatmap.max() if heatmap.max() != 0 else 1

    return heatmap
