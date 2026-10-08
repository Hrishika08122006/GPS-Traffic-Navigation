from ultralytics import YOLO
from pathlib import Path

# Load YOLO model
model = YOLO("yolo11n.pt")

# Path to our cleaned CCTV images
image_folder = Path("data/processed/train/images")

# Run vehicle detection
results = model.predict(
    source=str(image_folder),
    save=True,
    conf=0.40
)

print("Vehicle detection completed!")