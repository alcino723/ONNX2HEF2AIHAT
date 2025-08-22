import os
import argparse
from hailo_sdk_client import ClientRunner

def main(model_name, onnx_dir="Onnx", har_dir="Hailo", hw_arch="hailo8l"):
    # Paths
    onnx_path = os.path.join(onnx_dir, f"{model_name}.onnx")
    har_path = os.path.join(har_dir, f"{model_name}.har")

    # Ensure directories exist
    if not os.path.exists(onnx_path):
        raise FileNotFoundError(f"❌ ONNX file not found at: {onnx_path}")
    os.makedirs(har_dir, exist_ok=True)

    # Initialize runner
    runner = ClientRunner(hw_arch=hw_arch)

    # Translate model
    print(f"🔄 Translating ONNX model: {onnx_path}")
    hn, npz = runner.translate_onnx_model(onnx_path, model_name)

    # Save HAR
    runner.save_har(har_path)
    print(f"✅ HAR file saved as {har_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert ONNX model to HAR using Hailo SDK")
    parser.add_argument("model_name", help="Name of the model (without .onnx extension)")
    parser.add_argument("--onnx_dir", default="Onnx", help="Directory containing ONNX models")
    parser.add_argument("--har_dir", default="Hailo", help="Directory to save HAR files")
    parser.add_argument("--hw_arch", default="hailo8l", help="Target Hailo hardware architecture")

    args = parser.parse_args()
    main(args.model_name, args.onnx_dir, args.har_dir, args.hw_arch)