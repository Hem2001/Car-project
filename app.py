import sys
# This trick blocks the 'lap' error on the web server
sys.modules['lap'] = None 

import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

st.set_page_config(page_title="Hem's Vehicle Tracker", layout="wide")

st.title("🚗 Vehicle Detection & Counter")
st.write("### 97% Accuracy Model - Created by Hem")

# Load your model
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
    
    # 2. Run Detection (Properly Indented)
    # Using track for the web app to keep detections constant
    results = model.track(img_array, persist=True, conf=0.4, imgsz=320, tracker="bytetrack.yaml")
    
    # 3. Plot and Display
    res_plotted = results[0].plot()
    st.image(res_plotted, caption='Detected Vehicles', use_container_width=True)
    
    # 4. Show Counts
    st.write("### 📊 Detection Results")
    counts = {}
    for c in results[0].boxes.cls:
        label = model.names[int(c)]
        counts[label] = counts.get(label, 0) + 1
    
    if counts:
        # Create columns to show counts neatly
        cols = st.columns(len(counts))
        for i, (label, count) in enumerate(counts.items()):
            cols[i].metric(label.upper(), count)
    else:
        st.write("No vehicles detected in this frame.")