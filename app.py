import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

# Page Config
st.set_page_config(page_title="Hem's Vehicle Tracker", layout="wide")

st.title("🚗 Vehicle Detection & Counter")
st.write("### 97% Accuracy Model - Created by Hem")

# Load your model safely
@st.cache_resource
def load_model():
    return YOLO('best.pt')

model = load_model()

# Option to use Webcam
img_file = st.camera_input("Take a photo of traffic to detect")

if img_file:
    # 1. Convert the file to an image YOLO can read
    img = Image.open(img_file)
    img_array = np.array(img)
    
    # 2. Run Prediction (This avoids the 'lap' error completely)
    # We use .predict instead of .track for 100% web stability
    results = model.predict(img_array, conf=0.4, imgsz=320)
    
    # 3. Plot and Display
    res_plotted = results[0].plot()
    st.image(res_plotted, caption='Detected Vehicles', use_container_width=True)
    
    # 4. Show Counts
    st.write("### 📊 Detection Results")
    counts = {}
    if len(results[0].boxes) > 0:
        for c in results[0].boxes.cls:
            label = model.names[int(c)]
            counts[label] = counts.get(label, 0) + 1
        
        # Display metrics
        cols = st.columns(len(counts))
        for i, (label, count) in enumerate(counts.items()):
            cols[i].metric(label.upper(), count)
    else:
        st.info("No vehicles detected. Try a different angle or closer shot!")