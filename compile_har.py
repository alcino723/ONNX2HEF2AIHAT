# optimize_har.py
from hailo_sdk_client import ClientRunner
import os

# user params
MODEL            = "Segformer"
HAR             = os.path.join("Hailo", MODEL)
HAR_IN          = os.path.join(HAR, f"{MODEL}_optimized.har")

runner = ClientRunner(har=HAR_IN)
hef = runner.compile()
file_name = os.path.join(HAR, f'{MODEL}.hef')
with open(file_name, 'wb') as f:
    f.write(hef)
print(f"\n✅ HEF file saved as {MODEL}.hef in {HAR} directory.")