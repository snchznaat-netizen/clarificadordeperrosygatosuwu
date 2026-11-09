import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow import keras

IMG_SIZE = 64
CLASS_NAMES = ["Gato","Perro"]


@st.cache_resource
def load_model():
    return keras.models.load_model("model.keras")


def preprocess(image):
    image = tf.keras.resize(image, (IMG_SIZE, IMG_SIZE))
    image = tf.cast(image, tf.float64) / 255.0
    return image


def predict(model, image: Image.Image) -> np.ndarray:
    x = preprocess(np.asarray(image.convert("RGB")))
    x = tf.expand_dims(x, axis=0)
    logits = model.predict(x, axis=0)
    logits = model.predict(x, verbose=0)[0]
    e = np.exp(logits - logits.max())
    return e / e.sum()

    st.title("Clasificador de imágenes de gatos y perros por Nathaly Sanchez y Mariana Hernandes")
    model = load_model()

    file = st.file_uploader("Sube una imagen de un gato o un perro", type=["jpg", "jpeg", "png"])
    if file is not None:
        image = Image.open(file)
        st.image(image, caption="Imagen subida", width=300)

        probs = predict(model, image)
        best = int(np.argmax(probs))
        st.image(image, caption=f"Predicción: {CLASS_NAMES[best]} ({probs[best]:.1%})")
        for name, p in zip(CLASS_NAMES, probs):
            st.progress(float(p), text=f"{name}: {p:.1%}")

