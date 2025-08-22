# A step by step "guide" for deploying your custom model on the Raspberry pi AI HAT. 

Please note I spend over 20+ hours trying to get the damn thing to work and as of writing this guide, I still barely know what will work or what will not work. 
This step by step is a recreation of what worked for me, hopefully this quick and dirty guide work for you.

## Part 1 : Converting Onnx to HEF

This guide is using `WSL2 Ubuntu 24.04` with `conda`

It is recommended to simplified your onnx first before conversion, but it is not a strict requirement.

My guide is focus on model train with input data normalize to range[0 - 1]. If you model is train with other normalization range, then you will have to do some experimenting on your own. 

### 1.0) Git Clone repository

git clone this repository. 

```bash
git clone https://github.com/alcino723/ONNX2HEF2AIHAT.git
```

The starting folder structures look like this : 

- PROJECT
  - Onnx
    - PLACE YOUR ONNX HERE
  - Hailo
    - model_script.alls
  - Images
    - PLACE YOUR CALIBRATION IMAGE HERE
  - onnx2har.py
  - optimize_har.py
  - compile_har.py

Place your onnx under the Onnx folder.

Place your calibration images (images you use to evaluate your model) under the Images folder. 

### 1.0) Download hailo DFC

If you don't have a hailoai account please head over to https://hailo.ai/ and create your account first.

Once you have an account, login and go to developer zone.

In developer zone go to Software Downloads.

 - Select Device : Hailo-8/8L
 - Software Sub-Package : Dataflow Compiler
 - Architecture : x86
 - OS : Linux
 - Python Version : 3.10
 - Filter by : Latest Release (Change to Archive if you couldn't find it)

Download the following file to Project directory
<img width="1994" height="210" alt="image" src="https://github.com/user-attachments/assets/4a17d40d-b67b-4bbe-802c-f3f997e2d331" />

### 1.1) Setting up environments 

To get started, it is best to create 2 new virtual environment. 1 for Hailo and 1 for cv2

Environment Hailo 

```bash
conda create -n Hailo python=3.10
```

Activate your environment.

```bash
conda activate Hailo
```

Your should see 

```bash 
(Hailo) YOUR_USER_NAME@DESKTOP:~$
```

Install Hailo DFC in the `Hailo` environment.

```bash 
pip install hailo_dataflow_compiler-3.32.0-py3-none-linux_x86_64.whl
```

---------------

Environment CV2

```bash
conda create -n CV2 python=3.10
```

Activate your environment.

```bash
conda activate CV2
```

Your should see 

```bash 
(CV2) YOUR_USER_NAME@DESKTOP:~$

```

Install `opencv-python` in the `CV2` environment

```bash
pip install opencv-python
```

### 1.4) Convert Onnx to HAR

Run the following script

```bash
python onnx2har.py YOUR_MODEL_NAME
```

Example :

If your onnx is called EXAMPLE.onnx, then run

```bash
python onnx2har.py EXAMPLE
```

When conversion is complete, YOUR_MODEL_NAME.har should be under the Hailo folder.

### 1.5) Calibration dataset 

Before running the optimization step, you will need to create a calibration set for the optimization process.



### 1.6) Optimized HAR 


```bash
python optimize_har.py YOUR_MODEL_NAME
```

Example :

If your har is called EXAMPLE.har, then run

```bash
python optimize_har.py EXAMPLE
```

If your model is train with data normalize to some other range that isn't [0 - 1] you will need to modify the `model_sciprt.alls` file before running the script. 
**Note : I am have tried with model that isn't normalize to [0 -1], I am not sure if this correct or not.**

Modify this line 

`normalize1 = normalization([0, 0, 0], [255, 255, 255])`

to 

`normalize1 = normalization([min, min, min], [max, max, max])` 

Per Color Channel

where min = your min range * 255

where max = your max range * 255






      


