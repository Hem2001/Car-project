import cv2
import imageio
import os
import easyocr
from ultralytics import YOLO
from datetime import datetime
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# 1. SETUP
print("⏳ Initializing System...")
model = YOLO('yolov8n.pt') 
reader_ocr = easyocr.Reader(['en'], gpu=False) 

# 2. Find Video
video_path = "test.mp4" 
for root, dirs, files in os.walk(os.getcwd()):
    if 'test.mp4' in files:
        video_path = os.path.join(root, 'test.mp4')
        break

# 3. Parameters
line_y = 700 
counter = 0
crossed_ids = set()
data_log = []
if not os.path.exists('plates_captured'): os.makedirs('plates_captured')

print("🚀 Running... Press 'Q' on the video window to stop.")
reader = imageio.get_reader(video_path)
cv2.namedWindow("HEM - Smart Traffic AI", cv2.WINDOW_NORMAL)

try:
    for frame_rgb in reader:
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        results = model.track(frame, persist=True, conf=0.2, classes=[2, 3, 5, 7, 8])
        
        cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 0, 255), 2)

        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            ids = results[0].boxes.id.int().cpu().numpy()
            clss = results[0].boxes.cls.int().cpu().numpy()

            for box, id, cls in zip(boxes, ids, clss):
                x1, y1, x2, y2 = map(int, box)
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                label = model.names[cls].upper()

                if cy > line_y and id not in crossed_ids:
                    crossed_ids.add(id)
                    counter += 1
                    
                    # 1. Define the crop immediately so it's never "undefined"
                    # We use max/min to stay inside the video boundaries
                    h, w, _ = frame.shape
                    vehicle_crop = frame[max(0, y1):min(h, y2), max(0, x1):min(w, x2)]
                    
                    plate_text = "----" # Default if OCR fails
                    
                    # 2. Attempt OCR
                    try:
                        # Resize crop slightly to help the AI "see" better
                        temp_crop = cv2.resize(vehicle_crop, (0,0), fx=1.5, fy=1.5)
                        ocr_result = reader_ocr.readtext(temp_crop, allowlist='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                        if ocr_result:
                            plate_text = ocr_result[0][1].upper()
                    except:
                        plate_text = "ERROR"
                    
                    print(f"✅ {label} (ID: {id}) | PLATE: {plate_text}")
                    
                    # 3. Save Data
                    data_log.append({
                        "ID": id, 
                        "Type": label, 
                        "Plate": plate_text, 
                        "Time": datetime.now().strftime("%H:%M:%S")
                    })
                    
                    # 4. Save Image
                    img_name = f"plates_captured/veh_{id}_{label}.jpg"
                    cv2.imwrite(img_name, vehicle_crop)

        cv2.putText(frame, f"COUNT: {counter}", (50, 100), 0, 1.2, (0, 255, 0), 3)
        cv2.imshow("HEM - Smart Traffic AI", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"⚠️ Error: {e}")

finally:
    if data_log:
        pd.DataFrame(data_log).to_csv("traffic_analysis_report.csv", index=False)
        print("✅ Report saved.")
    
    cv2.destroyAllWindows()
    reader.close()