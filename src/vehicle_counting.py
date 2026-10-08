from ultralytics import YOLO
from pathlib import Path
import csv

# Load YOLO model
model = YOLO("yolo11n.pt")

# Folder containing our cleaned CCTV images
image_folder = Path("data/processed/train/images")

# Output CSV
output_file = Path("outputs/traffic_counts.csv")
output_file.parent.mkdir(parents=True, exist_ok=True)

# COCO classes we are interested in
vehicle_classes = {
    2: "car",
    5: "bus",
    7: "truck"
}

# Store results
rows = []

# Process every image
for image_file in image_folder.glob("*"):

    results = model.predict(
        source=str(image_file),
        conf=0.40,
        verbose=False
    )

    counts = {
        "car": 0,
        "bus": 0,
        "truck": 0
    }

    # Read detected classes
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])

            if class_id in vehicle_classes:
                vehicle_name = vehicle_classes[class_id]
                counts[vehicle_name] += 1

    total = sum(counts.values())

    rows.append({
        "image": image_file.name,
        "cars": counts["car"],
        "buses": counts["bus"],
        "trucks": counts["truck"],
        "total_vehicles": total
    })

# Save CSV
with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "image",
            "cars",
            "buses",
            "trucks",
            "total_vehicles"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print("Vehicle counting completed!")
print("Images processed:", len(rows))
print("CSV saved to:", output_file)