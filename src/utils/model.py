import tensorflow as tf
import tensorflow_hub as hub
from src.utils.image import load_categories
import numpy as np



def load_model(model_dir):
    model = tf.keras.models.load_model(model_dir, custom_objects={'KerasLayer':hub.KerasLayer})
    print("Model has been loaded")

    return model



def predict_func(model_dir, image):
    model = load_model(model_dir)
    classes = load_categories()
    probabilities = model.predict(np.asarray([image]))[0]
    class_idx = np.argmax(probabilities)
    
    
    return {classes[class_idx]: probabilities[class_idx]}


