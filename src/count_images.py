from pathlib import Path
import shutil

# Raw dataset paths
train_images = Path("data/raw/train/images")
train_labels = Path("data/raw/train/labels")

# Processed dataset paths
processed_images = Path("data/processed/train/images")
processed_labels = Path("data/processed/train/labels")

# Create processed folders
processed_images.mkdir(parents=True, exist_ok=True)
processed_labels.mkdir(parents=True, exist_ok=True)

# Copy only images that have a matching label
copied = 0

for image_file in train_images.glob("*"):
    label_file = train_labels / f"{image_file.stem}.txt"

    if label_file.exists():
        shutil.copy2(image_file, processed_images / image_file.name)
        shutil.copy2(label_file, processed_labels / label_file.name)
        copied += 1

print("Clean dataset created!")
print("Image-label pairs copied:", copied)