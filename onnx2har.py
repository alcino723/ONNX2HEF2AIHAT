from hailo_sdk_client import ClientRunner
import os

MODEL           = "Segformer"
ONNX            = os.path.join("Onnx", MODEL)
ONNX_PATH       = os.path.join(ONNX, f"{MODEL}_simplified.onnx")
HW_ARCH         = 'hailo8l'
HAR             = os.path.join("Hailo", MODEL)
os.makedirs(HAR, exist_ok=True)

runner = ClientRunner(hw_arch=HW_ARCH)
hn, npz = runner.translate_onnx_model(
    ONNX_PATH,
    MODEL
)

save_file = os.path.join(HAR, f"{MODEL}.har")
runner.save_har(save_file)
print(f"✅ HAR file saved as {MODEL}.har in {HAR} directory.")
