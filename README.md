# A step by step "guide" for deploying your custom model on the Raspberry pi AI HAT. 

Please note I spend over 20+ hours trying to get the damn thing to work and as of writing this guide, I still barely know what work or what will not work. 
This step by step is a recreation of what worked for me, I have no idea if it will work for you. 


## Part 1 : Converting Onnx to HEF

This guide is using WSL2 Ubuntu 24.04 with conda

### 1.0) Download hailo DFC


### 1.1) setting up a new environment

To get started, it is best to create a new virtual environment.

```bash
conda create -n YOUR_ENV_NAME python=3.10
```

After
