# A step by step "guide" for deploying your custom model on the Raspberry pi AI HAT. 

Please note I spend over 20+ hours trying to get the damn thing to work and as of writing this guide, I still barely know what will work or what will not work. 
This step by step is a recreation of what worked for me, I have no idea if it will work for you. 


## Part 1 : Converting Onnx to HEF

This guide is using `WSL2 Ubuntu 24.04` with `conda`

### 1.0) Download hailo DFC

If you don't have a hailoai account please head over to https://hailo.ai/ and create your account first.

Once you have an account, login and go to developer zone.

In developer zone go to Software Downloads.

 - Select Device : Hailo-8/8L
 - Software Sub-Package : Dataflow Compiler
 - Architecture : x86
 - OS : Linux
 - Python Version : 3.10
 - Filter by : Archive

Download the following file to your wls2
<img width="1992" height="174" alt="image" src="https://github.com/user-attachments/assets/335aff6c-2715-4548-8b3a-6528111ca9a4" />

### 1.1) Setting up a new environment

To get started, it is best to create a new virtual environment.

```bash
conda create -n YOUR_ENV_NAME python=3.10
```

Activate your environment

```bash
conda activate YOUR_ENV_NAME 
```

Your should see 

```bash 
(YOUR_ENV_NAME) YOUR_USER_NAME@DESKTOP:~$
```

### 1.2) Install Hailo DFC

Navigate to directory where `hailo_dataflow_compiler-3.31.0-py3-none-linux_x86_64.whl` is placed

Install Hailo DFC by running
```bash 
pip install hailo_dataflow_compiler-3.31.0-py3-none-linux_x86_64.whl
```

### 1.3) Project Structure

If you want to my code with minimium modification, please follow my starting folder structures. 

- PROJECT
  - Onnx
    - YOUR_MODEL_NAME
      - YOUR_MODEL_NAME.onnx
  - Hailo
    - model_script.alls
  - onnx2har.py
  - optimize_har.py
  - compile_har.py


      
      


