from ultralytics import YOLO
import cv2
import numpy as np

# 1. Load your model
model = YOLO('best.pt')

# 2. Open the webcam
cap = cv2.VideoCapture(0)

print("Live Detection Started... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # 3. RUN DETECTION (We use .predict to avoid the 'lap' tracking error)
    # This will give you boxes and labels, but without the 'ID' numbers for now
    # Fine-tuned for shaky/handheld video
    # Force the tracker to use scipy instead of the broken 'lap' library
    results = model.track(
        frame, 
        imgsz=320, 
        conf=0.3, 
        persist=True, 
        tracker="bytetrack.yaml"
    )

    for r in results:
        # Create a dictionary to count detections for this frame
        counts = {}
        for c in r.boxes.cls:
            label = model.names[int(c)]
            counts[label] = counts.get(label, 0) + 1
        
        # Draw the boxes and labels
        annotated_frame = r.plot()

        # 4. DRAW THE COUNTER TEXT (Custom HEM Header)
        cv2.putText(annotated_frame, "VEHICLE COUNT BY HEM:", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        y_offset = 40
        for vehicle, count in counts.items():
            text = f"{vehicle}: {count}"
            cv2.putText(annotated_frame, text, (10, y_offset + 20), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            y_offset += 25

        # Show the frame
        cv2.imshow("Real-Time Traffic Monitor", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()