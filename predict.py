import cv2
import imageio
import os
from ultralytics import YOLO
import pandas as pd
from datetime import datetime

# 1. Load your Model
model = YOLO('best.pt')

# 2. THE FORCE SEARCHER
video_path = None
print("🔍 Searching for your video file...")

# This scans your entire project folder for 'test.mp4'
for root, dirs, files in os.walk(os.getcwd()):
    if 'test.mp4' in files:
        video_path = os.path.join(root, 'test.mp4')
        break

if not video_path:
    print("❌ ERROR: I scanned every folder but could not find 'test.mp4'.")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Folders I see: {os.listdir('.')}")
    exit()

# 3. OPENING THE VIDEO
print(f"✅ FOUND IT! Path: {video_path}")
print("🚀 Starting AI Tracking...")
try:
    reader = imageio.get_reader(video_path)
except Exception as e:
    print(f"❌ Failed to read video: {e}")
    exit()

# 4. SETTINGS
line_y = 700 
counter = 0
crossed_ids = set()
data_log = []

cv2.namedWindow("Hem's Vehicle Counter", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hem's Vehicle Counter", 1280, 720)

# 5. THE MAIN LOOP
for frame_rgb in reader:
    frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    results = model.track(frame, persist=True, conf=0.4)
    cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 255, 0), 3)

    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.int().cpu().numpy()
        clss = results[0].boxes.cls.int().cpu().numpy()

        for box, id, cls in zip(boxes, ids, clss):
            cx, cy = int((box[0] + box[2]) / 2), int((box[1] + box[3]) / 2)
            label = model.names[cls]
            if cy > line_y and id not in crossed_ids:
                crossed_ids.add(id)
                counter += 1
                data_log.append({"ID": id, "Type": label, "Time": datetime.now().strftime("%H:%M:%S")})

    cv2.putText(frame, f"COUNT: {counter}", (50, 80), 0, 2, (0, 255, 0), 4)
    cv2.imshow("Hem's Vehicle Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
reader.close()