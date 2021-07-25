
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/haanhvu010799/Code-KLTN">
    <img src="https://tuoitre.uit.edu.vn/wp-content/uploads/2015/07/logo-uit.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Xây dụng mô hình Yolov3, Yolov4 trên Window hoặc Linux</h3>

  <p align="center">
    Nền tảng Darknet hỗ trợ Train model Yolov3, Yolov4. Vì quá trình thực hiện dài và tiêu tốn tài nguyên máy tính, cho nên phải train trên Google Colab. Để tránh xảy ra lỗi, tốt nhất phải train trên Linux. 
    <br />
    Branch này là branch gốc, dùng để đào tạo mô hình, chị sử dụng trên Laptop, nếu muốn sử dụng trên thiết bị nhúng cần tối ưu lại qua định dạng khác.
    <br />
    <a href="https://drive.google.com/drive/folders/10h3T-nEOYtlPWOzyAg61bO8PoTDAY0ON?usp=sharing">View Demo</a>
    ·
    <a href="https://github.com/haanhvu010799/Code-KLTN/tree/TensorRT">Model TensorRT triển khai trên Jetson Nano</a>
    ·
    <a href="https://github.com/haanhvu010799/Code-KLTN">Model huấn luyện Yolov3, Yolov4</a>
    ·
    <a href="https://github.com/haanhvu010799/Code-KLTN/tree/yolov5">Model Yolov5</a>
    ·
    <a href="https://github.com/haanhvu010799/Code-KLTN/tree/TFlite">Model Tflite được tối ưu hóa từ Yolo</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Mục lục</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">Các yêu cầu cơ bản</a>
      <ul>
        <!-- <li><a href="#built-with">Phần mềm, công cụ cần có</a></li>
        <li> -->
      </ul>
    </li>
    <li>
      <a href="#getting-started">Bắt đầu thực hiện</a>
      <ul>
        <li><a href="#installation">Cài đặt thư viện</a></li>
        <li><a href="#prerequisites">Debug Darknet</a></li>
      </ul>
    </li>
    <li><a href="#usage">Huấn luyện mô hình</a></li>
    <li><a href="#roadmap">Cấu trúc thư mục</a></li>
    <li><a href="#contributing">Cách chạy mô hình</a></li>
    <!-- <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Các yêu cầu phải có cài đặt
- **CMake >= 3.18**: https://cmake.org/download/
- **Powershell** (already installed on windows): https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell
- **CUDA >= 10.2**: https://developer.nvidia.com/cuda-toolkit-archive (on Linux do [Post-installation Actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions))
- **OpenCV >= 2.4**: use your preferred package manager (brew, apt), build from source using [vcpkg](https://github.com/Microsoft/vcpkg) or download from [OpenCV official site](https://opencv.org/releases.html) (on Windows set system variable `OpenCV_DIR` = `C:\opencv\build` - where are the `include` and `x64` folders [image](https://user-images.githubusercontent.com/4096485/53249516-5130f480-36c9-11e9-8238-a6e82e48c6f2.png))
- **cuDNN >= 8.0.2** https://developer.nvidia.com/rdp/cudnn-archive (on **Linux** copy `cudnn.h`,`libcudnn.so`... as described here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux-tar , on **Windows** copy `cudnn.h`,`cudnn64_7.dll`, `cudnn64_7.lib` as described here https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installwindows )
- **GPU with CC >= 3.0**: https://en.wikipedia.org/wiki/CUDA#GPUs_supported
<!-- GETTING STARTED -->
## Thực hiện

Chạy các lệnh trên Terminal trong thư mục darknet 
### Cài đặt thư viện

1. Cái đặt công cụ pip để cài đặt
   ```sh
   sudo apt install python3-pip
   ```
2. Cài đặt các thư viện hỗ trợ
   ```sh
   pip3 install -r requirements-gpu.txt
   ```


### Debug
Sau khi có đầy đủ các công cụ hỗ trợ, cài Darknet theo hướng dẫn trong link dưới
  ```sh
  https://pjreddie.com/darknet/install/
  ```

## Huấn luyện mô hình
1. Dowload Dataset cùng Label để vào 1 thư mục firedata, chạy file TrainSplit.py để tách ra giữa lượng ảnh Train và Valid
  ```sh
   python3 trainsplit.py
   ```
2. Tải Pretrain Model tại đây, có nhiều sự lựa chọn
  ```sh
  https://github.com/AlexeyAB/darknet#pre-trained-models
  ```
3. Tạo hai file yolo.names và yolo.data
   ```sh
    echo "fire" > yolo.names
    echo classes=1 > yolo.data
    echo train=train.txt >> yolo.data
    echo valid=val.txt >> yolo.data
    echo names=yolo.names >> yolo.data
    echo backup=backup >> yolo.data
   ```
4. Train model
   ```sh
    ./darknet detector train yolo.data cfg/yolov4-tiny.cfg yolov4-tiny.conv.29 -dont_show 
   ```  
<!-- ROADMAP -->
## Cấu trúc thư mục
<pre>
<span></span>
darknet/
├─ backup/ # Nơi chứa Weights khi Train
├─ cfg/    # Nơi chứa các file cấu hình
├─ firedata/  # Dataset
├─ result/  # Kết quả train biểu diễn bằng đồ thị
├─ test/  # Chứa hình ảnh để test
├─ darknet.py # Detect trên ảnh
├─ darknet_video.py #Detect trên Video
    <!-- official/
   ├─ orbit/
   ├─ research/
   └── ... -->
</pre>


<!-- CONTRIBUTING -->
## Cách chạy mô hình
Trên linux sử dụng  `./darknet` trên terminal thay vì `darknet.exe`, ví dụ:`./darknet detector test ./yolo.data ./cfg/yolov4-tiny.cfg ./yolov4.weights`

- Yolo v4 COCO - **chạy ảnh**: `darknet.exe detector test yolo.data cfg/yolov4-tiny.cfg yolov4.weights -thresh 0.25`
- **Output coordinates** of objects: `darknet.exe detector test yolo.data yolov4-tiny.cfg yolov4.weights -ext_output dog.jpg`
- Yolo v4 COCO - **chạy video**: `darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights -ext_output test.mp4`
- Yolo v4 COCO - **chạy WebCam 0**: `darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights -c 0`
- Yolo v4 COCO for **net-videocam** - Smart WebCam: `darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights http://192.168.0.80:8080/video?dummy=param.mjpg`
- Yolo v4 - **lưu kết quả dưới dạng videofile res.avi**: `darknet.exe detector demo yolo.data cfg/yolov4-tiny.cfg yolov4.weights test.mp4 -out_filename res.avi`
- Kiểm tra accuracy: `darknet.exe detector map yolo.data cfg/yolov4-tiny.cfg backup\{tên file weights vừa train xong}`

<!-- ## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements --> 
