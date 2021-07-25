# Code-KLTN
mỗi branch là một model khác nhau
# tensorrt_demos
<p align="center">
    <p align="center">
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

* [Prerequisite](#prerequisite)
<!-- * [Demo #1: GoogLeNet](#googlenet)
* [Demo #2: MTCNN](#mtcnn)
* [Demo #3: SSD](#ssd) -->
<!-- =* [Demo #4: YOLOv3](#yolov3) -->
* [Thiết lập TensorRT với YOLOv4 hoặc Yolov3](#yolov4)
<!-- * [Demo #6: Using INT8 and DLA core](#int8_and_dla)
* [Demo #7: MODNet](#modnet) -->

<a name="prerequisite"></a>
Prerequisite
------------
* Yêu cầu 1: Phải thực hiện trên thiết bị Jetson Nano bản 2GB, hệ điều hành Jetpack phiên bản 4.5.1 
* Yêu cầu 2: TensorRT phiên bản từ 6 trở lên, ngoài ra phải cài Tensorflow phiên bản 2.3.0
* Yêu cầu 3: Có đầy đủ các thư viện cần thiết, xem danh sách <a href="https://github.com/haanhvu010799/Code-KLTN/blob/main/requirements-gpu.txt">tại đây</a>
* Yêu cầu 4: Sử dụng python 3.6.9 sẽ không xảy ra lỗi khi chạy mô hình

<a name="yolov4"></a>
Tối ưu hóa mô hình từ Yolov4
---------------

1. Cài đặt "pycuda" để hỗ trợ truy cập CUDA của card màn hình trong lúc sử dụng ngôn ngữ lập trình Python.
   ```shell
   $ cd ${HOME}/project/tensorrt_demos/ssd
   $ ./install_pycuda.sh
   ```

2. Cài đặt  **phiên bản "1.4.1" (các phiên bản khác sẽ bị lỗi trừ phiên bản này)** của python3  **"onnx"** module.  
   ```shell
   $ sudo pip3 install onnx==1.4.1
   ```

3. Truy cập thư mục "plugins/" và build file "yolo_layer" plugin.  Sau khi xong, file "libyolo_layer.so" sẽ được khởi tạo. Điều này giúp trong quá trình tối ưu, mô hình TensorRT nhận ra định dạng của Yolo và cải thiện tốc độ chuyển đổi định dạng.
   ```shell
   $ cd ${HOME}/project/tensorrt_demos/plugins
   $ make
   ```

4. Chuyển đổi từ Yolo4 -> Onnx -> TensorRT.  

   ```shell
   $ cd ${HOME}/project/tensorrt_demos/yolo
   $ ./download_yolo.sh
   $ python3 yolo_to_onnx.py -m yolov4-416
   $ python3 onnx_to_tensorrt.py -m yolov4-416
   ```
   Tên model yolo phải đặt tên lại theo cú pháp [Tên model]-[kích thước]. Ví dụ Yolov4-tiny có kích thước 416px, ta phải đặt tên là yolov4-tiny-416.weights
   Trong trường hợp lúc chuyển đổi sang định dạng onnx bị lỗi báo thiếu bộ nhớ hay có process song song đang chạy, tham khảo giải pháp <a href="https://github.com/jkjung-avt/tensorrt_demos/issues/344">tại đây</a>

5. Cách chạy mô hình TensorRT trên local
Thảm khảo cách truyền hình ảnh đầu vào tại file <a href="https://github.com/haanhvu010799/Code-KLTN/blob/TensorRT/utils/camera.py">utils/camera.py</a> để xem cách truyền thiết bị và đường dẫn
Model TensorRT thu được ở bước trên để nguyên trong thư mục Yolo.
   ```shell
   $ cd ${HOME}/project/tensorrt_demos
   $ python3 trt_yolo.py --[định dạng hình ảnh đầu vào] [đường dẫn] -m [tên model vừa tối ưu]
   ```
Ví dụ, chạy Camera được kết nối bằng USB để thu hình ảnh ta sử dụng:
    ```shell
   $ cd ${HOME}/project/tensorrt_demos
   $ python3 trt_yolo.py --usb 0 -m yolo4-tiny-416
   ```
Ví dụ, chạy Video định dạng mp4 với tên test.mp4:
    ```shell
   $ cd ${HOME}/project/tensorrt_demos
   $ python3 trt_yolo.py --video test.mp4 -m yolo4-tiny-416
   ```  
6. Cách chạy mô hình để chiếu Stream lên một Web Server
Trước tiên, tại mỗi file stream.py và app.py, người dùng cần vào và sửa đổi địa chỉ host. Kết quả sẽ giống như video Demo .Sau đó chạy đồng thời hai file:
    ```shell
   $ cd ${HOME}/project/tensorrt_demos
   $ python3 app.py --usb 0 -m yolo4-tiny-416
   $ python3 stream.py
   ```  
