import cv2
import numpy as np
from tensorflow.keras.models import load_model
import pickle

IMG_SIZE = 64

def load_model_and_labels():
    model = load_model("hieroglyph_cnn.h5")
    with open("label_encoder.pkl", "rb") as f:
        le = pickle.load(f)
    return model, le

def prepare_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    return img.reshape(1, IMG_SIZE, IMG_SIZE, 1) / 255.0
