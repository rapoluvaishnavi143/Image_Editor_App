import streamlit as st
import cv2
from PIL import Image
import numpy as np

import filters
import utils

st.set_page_config(page_title="Image Editor", page_icon="🖼️", layout="centered")

st.title("🖼️ Image Editing App")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img = utils.pil_to_cv(image)

    st.subheader("Original Image")
    st.image(image, channels="RGB")

    # Sidebar controls
    st.sidebar.title("Filters")

    blur_val = st.sidebar.slider("Blur", 1, 51, 1)
    bright_val = st.sidebar.slider("Brightness", -100, 100, 0)
    contrast_val = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
    sharp_val = st.sidebar.slider("Sharpness", 0.0, 1.0, 0.5)

    edge = st.sidebar.checkbox("Edge Detection")
    gray = st.sidebar.checkbox("Grayscale")

    # Apply filters step by step
    result = img.copy()

    result = filters.apply_blur(result, blur_val)
    result = filters.adjust_brightness(result, bright_val)
    result = filters.adjust_contrast(result, contrast_val)
    result = filters.apply_sharpness(result, sharp_val)

    if gray:
        result = filters.apply_grayscale(result)

    if edge:
        result = filters.apply_canny(result, 50, 150)

    st.subheader("Processed Image")
    st.image(result, channels="BGR")

    # Download button
    img_bytes = utils.cv_to_bytes(result)

    st.download_button(
        "Download Image",
        img_bytes,
        file_name="edited.png",
        mime="image/png"
    )
