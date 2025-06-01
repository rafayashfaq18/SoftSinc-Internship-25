import os
import shutil

def organize_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for file in os.listdir(source_dir):
        if file.endswith(".txt") or file.endswith(".csv"):
            full_path = os.path.join(source_dir, file)
            shutil.copy(full_path, os.path.join(target_dir, file))
    print(f"Copied .txt and .csv files to {target_dir}")

if __name__ == "__main__":
    organize_files("sample_data", "organized_files")