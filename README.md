
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/haanhvu010799/Code-KLTN">
    <img src="https://tuoitre.uit.edu.vn/wp-content/uploads/2015/07/logo-uit.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Xây dụng mô hình Yolov3, Yolov4 trên Window hoặc Linux</h3>

  <p align="center">
    Nền tảng Darknet hỗ trợ Train model Yolov3, Yolov4. Vì quá trình thực hiện dài và tiêu tốn tài nguyên máy tính, cho nên phải train trên Google Colab.
    <br />
    <!-- <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a> -->
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
    <li><a href="#contributing">Chức năng cụ thể</a></li>
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
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```


### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Cấu trúc thư mục
<pre>
<span></span>
darknet/
├─ backup/
├─ cfg/

    <!-- official/
   ├─ orbit/
   ├─ research/
   └── ... -->
</pre>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username