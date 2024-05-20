import json
import cv2
import numpy as np

def load_categories(dir):
    with open(dir, 'r') as f:
        cat_to_name = json.load(f)
        classes = list(cat_to_name.values())

    return classes    


def load_image(img):
    img = img.resize((299, 299))
    img = np.array(img) / 255.0  
    img = img.astype(np.float32)
    img = np.expand_dims(img, axis=0)
    return img
