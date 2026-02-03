from ultralytics import YOLO

# START FRESH to fix the Index Error
# yolov8n.pt is super light and perfect for your i5
model = YOLO('yolov8n.pt') 

if __name__ == '__main__':
    model.train(
        data='data.yaml',    # Ensure nc: 6 is in this file!
        epochs=30,           # 30 is a good goal
        imgsz=320,          # Keeps your laptop cool
        batch=8,            # Safe for RAM
        workers=0,          # Stable for Windows
        device='cpu',
        exist_ok=True       # Overwrites if the folder exists
    )