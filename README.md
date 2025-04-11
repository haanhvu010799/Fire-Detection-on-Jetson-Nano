# YOLOv3 & YOLOv4 Model Training on Windows or Linux

<p align="center">
  <a href="https://github.com/haanhvu010799/Code-KLTN">
    <img src="https://tuoitre.uit.edu.vn/wp-content/uploads/2015/07/logo-uit.png" alt="Logo" width="80" height="80">
  </a>
</p>

<h3 align="center">YOLOv3 & YOLOv4 Model Training on Windows/Linux using Darknet</h3>

<p align="center">
  This repository provides training implementations of YOLOv3 and YOLOv4 using the Darknet framework. Due to the computational intensity of training, we recommend using Google Colab and Linux for best compatibility and performance.
  <br /><br />
  <a href="https://drive.google.com/drive/folders/10h3T-nEOYtlPWOzyAg61bO8PoTDAY0ON?usp=sharing">📽️ View Demo</a>
  ·
  <a href="https://github.com/haanhvu010799/Code-KLTN/tree/TensorRT">🧠 TensorRT for Jetson Nano</a>
  ·
  <a href="https://github.com/haanhvu010799/Code-KLTN">📦 YOLOv3/YOLOv4 Training Code</a>
  ·
  <a href="https://github.com/haanhvu010799/Code-KLTN/tree/yolov5">🚀 YOLOv5 Version</a>
  ·
  <a href="https://github.com/haanhvu010799/Code-KLTN/tree/TFlite">📱 Optimized TFLite Version</a>
</p>

---

## 📚 Table of Contents

1. [System Requirements](#system-requirements)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Debugging Darknet](#debugging-darknet)
3. [Model Training](#model-training)
4. [Project Structure](#project-structure)
5. [Running the Model](#running-the-model)

---

## ✅ System Requirements

Make sure you have the following installed:

- **CMake ≥ 3.18**: https://cmake.org/download/
- **PowerShell** (pre-installed on Windows)
- **CUDA ≥ 10.2**: https://developer.nvidia.com/cuda-toolkit-archive
- **OpenCV ≥ 2.4**: https://opencv.org/releases.html  
  On Windows, set `OpenCV_DIR` environment variable to `C:\opencv\build`
- **cuDNN ≥ 8.0.2**: https://developer.nvidia.com/rdp/cudnn-archive  
  Follow installation instructions based on your OS.
- **GPU with Compute Capability ≥ 3.0**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported

---

## 🚀 Getting Started

Navigate to the `darknet/` directory and run the following:

### 📦 Installation

1. Install pip:
```bash
sudo apt install python3-pip
```

2. Install required Python packages:
```bash
pip3 install -r requirements-gpu.txt
```

### 🛠️ Debugging Darknet

Follow official Darknet installation instructions:
https://pjreddie.com/darknet/install/

---

## 🧠 Model Training

1. Download and place your dataset into the `firedata/` folder. Then split it:
```bash
python3 trainsplit.py
```

2. Download pre-trained models from:
https://github.com/AlexeyAB/darknet#pre-trained-models

3. Create configuration files:
```bash
echo "fire" > yolo.names
echo classes=1 > yolo.data
echo train=train.txt >> yolo.data
echo valid=val.txt >> yolo.data
echo names=yolo.names >> yolo.data
echo backup=backup >> yolo.data
```

4. Start training:
```bash
./darknet detector train yolo.data cfg/yolov4-tiny.cfg yolov4-tiny.conv.29 -dont_show
```

---

## 📁 Project Structure

```
darknet/
├── backup/           # Trained weight files
├── cfg/              # YOLO configuration files
├── firedata/         # Dataset and labels
├── result/           # Training graphs
├── test/             # Test images
├── darknet.py        # Image detection script
├── darknet_video.py  # Video detection script
```

---

## ▶️ Running the Model

### On Linux:
```bash
./darknet detector test ./yolo.data ./cfg/yolov4-tiny.cfg ./yolov4.weights
```

### On Windows:
```cmd
darknet.exe detector test yolo.data cfg/yolov4-tiny.cfg yolov4.weights -thresh 0.25
```

### Other Use Cases:

- Output object coordinates:
```cmd
darknet.exe detector test yolo.data yolov4-tiny.cfg yolov4.weights -ext_output dog.jpg
```

- Video detection:
```cmd
darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights test.mp4
```

- Webcam detection:
```cmd
darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights -c 0
```

- IP camera stream:
```cmd
darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights http://192.168.0.80:8080/video?dummy=param.mjpg
```

- Save detection results to video:
```cmd
darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights test.mp4 -out_filename res.avi
```

- Evaluate model accuracy:
```cmd
darknet.exe detector map yolo.data cfg/yolov4-tiny.cfg backup\your_weight_file.weights
```

---

Feel free to contribute or explore other branches for different deployment targets!
