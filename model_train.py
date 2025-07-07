import os
import cv2
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

IMG_SIZE = 64
DATA_DIR = "dataset_example"

def load_data():
    images, labels = [], []
    for fname in os.listdir(DATA_DIR):
        if fname.endswith(".jpg"):
            label = fname.split("_")[0]
            img = cv2.imread(os.path.join(DATA_DIR, fname), cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            images.append(img)
            labels.append(label)
    images = np.array(images).reshape(-1, IMG_SIZE, IMG_SIZE, 1) / 255.0
    le = LabelEncoder()
    labels_enc = le.fit_transform(labels)
    return train_test_split(images, labels_enc, test_size=0.2, random_state=42), le

(trainX, testX, trainY, testY), le = load_data()

model = Sequential([
    Conv2D(32, (3,3), activation="relu", input_shape=(IMG_SIZE,IMG_SIZE,1)),
    MaxPooling2D(),
    Conv2D(64, (3,3), activation="relu"),
    MaxPooling2D(),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(len(le.classes_), activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(trainX, trainY, epochs=10, validation_data=(testX, testY))
model.save("hieroglyph_cnn.h5")

# Simpan Label Encoder
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("✅ Model dan label encoder telah disimpan.")
print("🧠 Classes:", list(le.classes_))
