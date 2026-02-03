from ultralytics import YOLO
import cv2

# 1. Load your trained model
model = YOLO(r'C:\Users\heman\car project\runs\detect\train\weights\best.pt')

# 2. Open the webcam (0 is default)
cap = cv2.VideoCapture(0)

print("Live Detection with Counter Started... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Run detection (keep imgsz=320 for speed)
    results = model.predict(frame, imgsz=320, conf=0.5, stream=True)

    for r in results:
        # Create a dictionary to count detections for this frame
        counts = {}
        for c in r.boxes.cls:
            label = model.names[int(c)]
            counts[label] = counts.get(label, 0) + 1
        
        # Draw the boxes and labels
        annotated_frame = r.plot()

        # Create the counter text
        y_offset = 40
        cv2.putText(annotated_frame, "LIVE VEHICLE COUNT:", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
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