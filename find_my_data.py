import os

# This script searches your project for the images folder
project_root = r"C:\Users\heman\car project"

print("Searching for your dataset structure...")
found = False

for root, dirs, files in os.walk(project_root):
    # We are looking for the folder that contains 'train' and 'val'
    if "train" in dirs and "val" in dirs:
        # Check if they have images inside
        train_img_path = os.path.join(root, "train", "images")
        if os.path.exists(train_img_path):
            print("\n✅ FOUND THE DATASET!")
            print(f"Copy this line into your data.yaml 'path' section:")
            print(f"path: \"{root.replace('\\', '/')}\"")
            found = True
            break

if not found:
    print("\n❌ COULD NOT FIND DATASET.")
    print("Make sure you have folders named 'train' and 'val' inside 'datasets/car_data'.")