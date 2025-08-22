import os
import argparse
from hailo_sdk_client import ClientRunner

def compile_har_to_hef(model_name, har_dir="Hailo", output_dir="Hailo"):
    # Input HAR path
    har_in = os.path.join(har_dir, f"{model_name}_optimized.har")
    if not os.path.exists(har_in):
        raise FileNotFoundError(f"❌ HAR file not found at: {har_in}")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Output HEF path
    hef_out = os.path.join(output_dir, f"{model_name}.hef")

    # Initialize runner and compile
    print(f"📦 Loading HAR: {har_in}")
    runner = ClientRunner(har=har_in)

    print(f"⚙️  Compiling HAR → HEF...")
    hef = runner.compile()

    # Save HEF
    with open(hef_out, 'wb') as f:
        f.write(hef)

    print(f"✅ HEF file saved as: {hef_out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile a HAR file into a HEF file using Hailo SDK")
    parser.add_argument("model_name", help="Base name of the model (without extension)")
    parser.add_argument("--har_dir", default="Hailo", help="Directory containing the HAR file")
    parser.add_argument("--output_dir", default="Hailo", help="Directory to save the HEF file")

    args = parser.parse_args()
    compile_har_to_hef(args.model_name, args.har_dir, args.output_dir)