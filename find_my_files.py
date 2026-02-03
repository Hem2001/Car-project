import os

# This script will list every single folder in your project
# so we can see the exact spelling.
start_path = r"C:\Users\heman\car project"

print("--- FOLDER LIST ---")
for root, dirs, files in os.walk(start_path):
    # Only look at the first 2 levels deep to keep it clean
    level = root.replace(start_path, '').count(os.sep)
    if level < 3:
        indent = ' ' * 4 * level
        print(f"{indent}[FOLDER] {os.path.basename(root)}")
        # Check for images inside
        if "images" in dirs:
            print(f"{indent}    ⭐ FOUND IMAGES HERE!")