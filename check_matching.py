import os

train_img_path = r"C:\Users\heman\car project\my_datasets\car_data\train\images"
train_lbl_path = r"C:\Users\heman\car project\my_datasets\car_data\train\labels"

images = {os.path.splitext(f)[0] for f in os.listdir(train_img_path) if f.endswith(('.jpg', '.png', '.jpeg'))}
labels = {os.path.splitext(f)[0] for f in os.listdir(train_lbl_path) if f.endswith('.txt')}

print(f"Images found: {len(images)}")
print(f"Labels found: {len(labels)}")

missing_labels = images - labels
if missing_labels:
    print(f"❌ {len(missing_labels)} images are missing labels! Example: {list(missing_labels)[0]}")
else:
    print("✅ All filenames match!")