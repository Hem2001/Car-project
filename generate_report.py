from fpdf import FPDF

class ProjectReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'AI Vehicle Detection Project Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = ProjectReport()
pdf.add_page()
pdf.set_font("Arial", size=12)

# --- SECTION: OVERVIEW ---
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "1. Project Overview", 0, 1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 7, "This project involves training a YOLOv8 computer vision model to detect and count five types of vehicles (Car, Rickshaw, Motorbike, Truck, and Van) in real-time traffic video.")
pdf.ln(5)

# --- SECTION: MISTAKES & LEARNINGS ---
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "2. Challenges & Mistakes Overcome", 0, 1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 7, 
    "- Problem: Initial training with 640px images caused the i5 CPU to overheat and estimated 15+ hours of training.\n"
    "- Solution: Reduced Image Size to 320px, which sped up training by 4x without sacrificing detection quality.\n"
    "- Problem: Encountered '100+ errors' related to pathing and Python environments.\n"
    "- Solution: Fixed by navigating to the correct project directory and standardizing the ultralytics environment.")
pdf.ln(5)

# --- SECTION: RESULTS ---
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "3. Exact Model Performance", 0, 1)
pdf.set_font("Arial", size=10)

# Table Header
pdf.cell(40, 10, "Class", 1)
pdf.cell(40, 10, "Precision", 1)
pdf.cell(40, 10, "Recall", 1)
pdf.cell(40, 10, "mAP50 (Accuracy)", 1)
pdf.ln()

# Table Data
results = [
    ["All Classes", "0.968", "0.922", "0.972"],
    ["Car", "0.959", "0.896", "0.955"],
    ["Rickshaw", "0.981", "0.910", "0.979"],
    ["Motorbike", "0.973", "0.978", "0.992"],
    ["Van (Lowest)", "0.937", "0.875", "0.945"]
]

for row in results:
    for item in row:
        pdf.cell(40, 10, item, 1)
    pdf.ln()

pdf.ln(5)
pdf.set_font("Arial", 'B', 11)
pdf.cell(0, 10, "Final Inference Speed: 23.3ms per image (42 FPS)", 0, 1)

# --- SECTION: OUTPUT ---
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "4. Current Capabilities", 0, 1)
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 7, "The model successfully detects vehicles live through the webcam and provides a real-time count on the display. All results are saved in the 'runs/detect/predict' directory.")

# Save the PDF
pdf.output("Vehicle_Detection_Report.pdf")
print("Successfully created 'Vehicle_Detection_Report.pdf' in your folder!")