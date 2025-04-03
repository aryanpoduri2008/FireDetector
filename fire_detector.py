import tensorflow as tf
import numpy as np
import cv2
from twilio_sms import *

IMG_SIZE = (224, 224)
model = tf.keras.Sequential([
    tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet'),
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.load_weights("fire_model.weights.h5")
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, IMG_SIZE)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img


def predict_fire(image_path):
    img = preprocess_image(image_path)
    prediction = model.predict(img)

    if prediction >= 0.5:
        print("No fire detected. " + str(prediction))
    else:
        print("Fire Detected!: " + str(prediction))
        trigger_emergency_call()