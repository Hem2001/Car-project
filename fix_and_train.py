import os
from ultralytics import YOLO

def find_path(name):
    for root, dirs, files in os.walk(r"C:\Users\heman\car project"):
        if name in dirs:
            return os.path.join(root, name)
    return None

def main():
    # 1. Automatically find your data folder
    actual_val_path = find_path("val")
    
    if actual_val_path:
        # Get the parent of 'val', which should be 'car_data' or similar
        data_root = os.path.dirname(actual_val_path)
        print(f"✅ Found your data at: {data_root}")
        
        # 2. Update your data.yaml automatically with the FOUND path
        yaml_content = f"""
path: "{data_root.replace('\\', '/')}"
train: train/images
val: val/images
names:
  0: car
"""
        with open("data.yaml", "w") as f:
            f.write(yaml_content)
        print("✅ Updated data.yaml with the correct path.")

        # 3. Start Training
        model = YOLO("yolo11n.pt")
        model.train(data="data.yaml", epochs=100, imgsz=640, device="cpu", workers=0)
    else:
        print("❌ Still can't find a folder named 'val'. Please check your sidebar!")

if __name__ == "__main__":
    main()