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
*

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