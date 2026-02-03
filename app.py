import sys
# This trick blocks the 'lap' error on the web server
sys.modules['lap'] = None 

import streamlit as st
from ultralytics import YOLO
# ... the rest of your code ...import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

st.title("Vehicle Detection & Counter")
st.write("97% Accuracy Model - Created by Hem")

# Load your model
model = YOLO('best.pt')

# Option to use Webcam
img_file = st.camera_input("Take a photo of traffic to detect")

if img_file:
    # Convert the file to an image YOLO can read
    img = Image.open(img_file)
    img_array = np.array(img)
    
    # Run Detection
    # Using track for the web app to keep detections constant
    # Faster tracking for the web
results = model.track(img_array, persist=True, conf=0.4, imgsz=320, tracker="bytetrack.yaml")
    
    # Show Results
    res_plotted = results[0].plot()
    st.image(res_plotted, caption='Detected Vehicles', use_container_width=True)
    
    # Show Counts
    counts = {}
    for c in results[0].boxes.cls:
        label = model.names[int(c)]
        counts[label] = counts.get(label, 0) + 1
    st.write("Live Count:", counts)