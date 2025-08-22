import os
import argparse
from hailo_sdk_client import ClientRunner

def optimize_har(model_name, har_dir="Hailo", calib_path="calib_set.npy", alls_file="model_script.alls"):
    # Paths
    har_in = os.path.join(har_dir, f"{model_name}.har")
    har_out = os.path.join(har_dir, f"{model_name}_optimized.har")
    alls_path = os.path.join(har_dir, alls_file)
    calib_path = os.path.join(har_dir, calib_path)
    
    # Validate inputs
    if not os.path.exists(har_in):
        raise FileNotFoundError(f"❌ HAR file not found at: {har_in}")
    if not os.path.exists(alls_path):
        raise FileNotFoundError(f"❌ Model script (.alls) not found at: {alls_path}")
    if not os.path.exists(calib_path):
        raise FileNotFoundError(f"❌ Calibration file not found at: {calib_path}")

    # Initialize runner
    runner = ClientRunner(har=har_in)

    # Load model script
    print(f"🔧 Loading model script: {alls_path}")
    runner.load_model_script(model_script=alls_path)

    # Optimize with calibration data
    print(f"🚀 Optimizing HAR: {har_in}")
    runner.optimize(calib_data=calib_path)

    # Save optimized HAR
    runner.save_har(har_out)
    print(f"\n✅ Optimized HAR file saved as: {har_out}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize a HAR file using Hailo SDK")
    parser.add_argument("model_name", help="Base name of the model (without extension)")
    parser.add_argument("--har_dir", default="Hailo", help="Directory containing HAR and ALLS files")
    parser.add_argument("--calib_path", default="calib_set.npy", help="Path to the calibration data file")
    parser.add_argument("--alls_file", default="model_script.alls", help="Name of the .alls model script file")
    
    args = parser.parse_args()
    optimize_har(args.model_name, args.har_dir, args.calib_path, args.alls_file)