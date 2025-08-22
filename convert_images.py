import os
import cv2
import numpy as np
import argparse

def build_calibration_set(src_dir="Images", target_size=(512, 512), output_file="calib_set.npy"):
    # Ensure Hailo folder exists
    hailo_dir = "Hailo"
    os.makedirs(hailo_dir, exist_ok=True)

    # Force output path into Hailo folder
    output_path = os.path.join(hailo_dir, os.path.basename(output_file))

    # Get sorted list of image files
    image_files = sorted(
        f for f in os.listdir(src_dir)
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
    )

    if not image_files:
        raise FileNotFoundError(f"No images found in {src_dir}")

    # Pre‑allocate array (float32 for most calibration tools)
    calib_dataset = np.zeros((len(image_files), target_size[1], target_size[0], 3), dtype=np.float32)

    for idx, fname in enumerate(image_files):
        img_path = os.path.join(src_dir, fname)
        img = cv2.imread(img_path)  # BGR by default

        if img is None:
            print(f"Warning: Failed to read {img_path}")
            continue

        # 🖼️ Resize
        resized = cv2.resize(img, target_size, interpolation=cv2.INTER_AREA)

        # 🔄 Convert BGR → RGB
        resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

        # Store as uint8 in float32 array
        calib_dataset[idx] = resized_rgb.astype(np.uint8)

        if idx == 0:  # sanity check
            print(f"First image shape: {resized_rgb.shape}, range: {resized_rgb.min()}–{resized_rgb.max()}")

    # Save to .npy
    np.save(output_path, calib_dataset)
    print(f"✅ Saved calibration dataset: {output_path} ({calib_dataset.shape})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create calibration dataset from images")
    parser.add_argument("--src_dir", default="Images", help="Directory containing input images")
    parser.add_argument("--width", type=int, default=512, help="Target width")
    parser.add_argument("--height", type=int, default=512, help="Target height")
    parser.add_argument("--output", default="calib_set.npy", help="Output .npy file name (will be placed in Hailo/)")
    
    args = parser.parse_args()
    build_calibration_set(args.src_dir, (args.width, args.height), args.output)