=# 🚗 Real-Time Vehicle Analytics & Monitoring System

### **97.2% Accuracy Model | YOLOv8 | Computer Vision**

An advanced Computer Vision solution designed to transform standard video feeds into actionable traffic data. This project uses deep learning to detect, track, and count vehicles in real-time with high precision.

---

## 🚀 Key Features
- **High-Precision Detection:** Utilizes a custom-trained YOLOv8 model achieving **97.2% accuracy** across multiple vehicle classes (Cars, Vans, Motorbikes).
- **Intelligent Trip-Wire Logic:** Engineered a virtual counting line (Trip-Wire) that triggers only when a vehicle's centroid crosses the boundary, eliminating duplicate counts.
- **Persistent Tracking:** Implemented **ByteTrack** logic to maintain unique IDs for vehicles even during partial occlusions.
- **Automated Data Reporting:** Every detection is logged into a structured `traffic_analysis_report.csv` with timestamps and vehicle types for long-term analytics.
- **Cross-Platform Compatibility:** Designed to handle high-resolution (1080p) footage via stable decoders like `imageio` and `FFmpeg`.

---

## 📽️ Project Demo
*(Optional: Drag and drop your 1-minute video here in the GitHub editor to show it on the page!)*

---

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **AI Framework:** Ultralytics YOLOv8
- **Computer Vision:** OpenCV, ImageIO
- **Data Management:** Pandas, CSV
- **Tracking:** ByteTrack

---

## 📂 Project Structure
```text
car-project/
├── asset/
│   └── test/
│       └── test.mp4           # High-resolution demo footage
├── best.pt                    # 97.2% Accuracy weights
├── predict.py                 # Main AI logic & Trip-wire counting
├── requirements.txt           # Environment dependencies
└── traffic_analysis_report.csv # Automatically generated data export



Technical Challenges & Model Observations
While developing this system, I encountered several real-world Computer Vision challenges. Below is how I addressed them:

1. Vehicle Classification Accuracy
Challenge: The model occasionally labeled Vans or SUVs as "Cars."

Insight: This is a common occurrence in high-angle CCTV footage. From a top-down perspective, the structural differences between a large car and a van are minimal, leading the model to default to the more frequent class ("Car").

Solution: Optimized the detection by lowering the confidence threshold to 0.15 and expanding the class filter to include Bus, Truck, and Van labels.

2. OCR (License Plate) Limitations
Challenge: Many vehicles resulted in a ---- (Empty) plate reading.

Insight: Effective OCR requires a high "Pixel-per-Foot" ratio. In this wide-angle dataset, the license plates often occupy less than 2% of the total frame, resulting in motion blur and pixelation that prevents text extraction.

Engineering Fix: Implemented a cv2.resize scaling factor and INTER_CUBIC interpolation to sharpen the vehicle crops before passing them to the EasyOCR engine.

3. Hardware Performance
Challenge: Processing high-resolution video with both Tracking and OCR caused significant CPU lag.

Solution: Designed an Event-Driven OCR logic. Instead of scanning every frame, the script only triggers the heavy OCR engine at the exact moment a vehicle crosses the virtual "trip-wire," saving approximately 70% of processing power.

python detect_photo.py
### 🏆 Final Check
Go to your GitHub URL in your browser. You should now see:
* Your new `detect_photo.py` file.
* The updated `predict.py`.
* A fresh "commit" timestamp from a few minutes ago.
