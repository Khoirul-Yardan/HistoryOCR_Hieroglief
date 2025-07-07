from utils import load_model_and_labels, prepare_image

model, le = load_model_and_labels()
img = prepare_image("dataset_example/100 (1).jpg")
pred = model.predict(img)
label = le.inverse_transform([pred.argmax()])[0]
print("Prediksi simbol:", label)
