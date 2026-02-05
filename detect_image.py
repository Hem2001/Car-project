import cv2
from ultralytics import YOLO
import os

# 1. Load your model
model = YOLO('yolov8n.pt')

# 2. Set the image path
image_path = 'test_image.jpg' 

if not os.path.exists(image_path):
    print(f"❌ Error: Could not find {image_path}")
else:
    # 3. Run Detection
    print(f"🔍 Analyzing {image_path}...")
    results = model.predict(image_path, conf=0.25)

    # 4. Process Results
    img = cv2.imread(image_path)
    
    if len(results[0].boxes) == 0:
        print("Empty: No vehicles detected.")
    else:
        print("✅ Detection Results:")
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            confidence = box.conf[0]
            
            print(f"- Found a {label.upper()} ({confidence:.2f})")
            
            # Draw on the original high-res image
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f"{label} {confidence:.2f}", (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)

    # --- RESIZE ONLY FOR DISPLAY ---
    # This keeps the image at 800px wide so it fits your monitor
    width = 800
    ratio = width / img.shape[1]
    height = int(img.shape[0] * ratio)
    display_img = cv2.resize(img, (width, height))

    # 5. Show the result
    cv2.imshow("Hem's Detection Result", display_img)
    print("\n👉 Click the image window and press any key to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()