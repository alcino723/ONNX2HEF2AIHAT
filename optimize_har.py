# optimize_har.py
from hailo_sdk_client import ClientRunner
import os

# user params
CALIB_PATH       = "aug_val/calib_set.npy"
MODEL            = "Segformer"
HAR              = os.path.join("Hailo", MODEL)
HAR_IN           = os.path.join(HAR, f"{MODEL}.har")
HAR_OUT          = os.path.join(HAR, f"{MODEL}_optimized.har")
ALLS_FILE        = os.path.join("Hailo", "model_script.alls")

runner = ClientRunner(har=HAR_IN)

runner.load_model_script(model_script=ALLS_FILE)

runner.optimize(calib_data=CALIB_PATH)
runner.save_har(HAR_OUT)
print(f"\n✅ Optimized HAR file saved as {HAR_OUT}_optimized.har in {HAR} directory.")