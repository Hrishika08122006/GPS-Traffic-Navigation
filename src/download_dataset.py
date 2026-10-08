from huggingface_hub import snapshot_download

dataset_path = snapshot_download(
    repo_id="PRAS4NTH/traffic-vehicle-detection",
    repo_type="dataset",
    local_dir="data/raw"
)

print("Dataset downloaded to:", dataset_path)