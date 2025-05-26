<a id="readme-top"></a>

<div align="center">

  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-273382?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
  [![Ultralytics YOLOv8](https://img.shields.io/badge/YOLOv8-800080?style=for-the-badge&logoColor=white)](https://ultralytics.com/)
  [![CVZone](https://img.shields.io/badge/cvzone-informational?style=for-the-badge&logoColor=white)](https://github.com/cvzone/cvzone)
  [![Numpy](https://img.shields.io/badge/Numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)

<br />

[![Email](https://img.shields.io/badge/dhanrajaayush123%40gmail.com-important?style=for-the-badge)](mailto:dhanrajaayush123@gmail.com)
[![Email](https://img.shields.io/badge/ayushdhanraj.work%40gmail.com-important?style=for-the-badge)](mailto:ayushdhanraj.work@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-d-1759461a1)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayush-2001-Dhanraj)
</div>


<br />
<div align="center">
  <img src="images/logo.jpg" alt="Project Logo" width="150">

  <h3 align="center">Real-time Parking Lot Vehicle Entry Counter</h3>

  <p align="center">
    A project demonstrating real-time counting of vehicles entering a parking lot using computer vision techniques.
    <br />
    <a href="https://github.com/Ayush-2001-Dhanraj/Object-Detection/tree/main/Parking%20Lot%20Vehicle%20Entry%20Counter#readme"><strong>View on GitHub</strong></a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This project implements a real-time system to accurately count vehicles (cars, motorcycles, buses, trucks) as they enter a designated parking area. It utilizes a pre-trained YOLOv8 model for real-time object detection to identify and classify vehicles in a video stream. The SORT algorithm is then employed for robust tracking of individual vehicles across frames. A defined virtual "entry line" triggers a count increment when a unique vehicle crosses it, preventing double-counting.

This project showcases skills in computer vision, object detection, object tracking, real-time video processing, and algorithm implementation. It demonstrates the application of these technologies to a practical problem in traffic monitoring and parking management.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project was built using the following key technologies:

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![OpenCV](https://img.shields.io/badge/OpenCV-273382?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
* [![Ultralytics YOLOv8](https://img.shields.io/badge/YOLOv8-800080?style=for-the-badge&logoColor=white)](https://ultralytics.com/)
* [![CVZone](https://img.shields.io/badge/cvzone-informational?style=for-the-badge&logoColor=white)](https://github.com/cvzone/cvzone)
* [![Numpy](https://img.shields.io/badge/Numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To run this project locally, follow these steps.

### Prerequisites

Ensure you have the following installed on your system:

* Python (>= 3.7)
* pip (Python package installer)

### Installation

1.  Clone the repository:
    ```sh
    git clone [https://github.com/Ayush-2001-Dhanraj/Object-Detection.git](https://github.com/Ayush-2001-Dhanraj/Object-Detection.git)
    ```

2.  Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: You might need to install PyTorch separately based on your system's CUDA availability. Refer to the [PyTorch website](https://pytorch.org/get-started/locally/) for specific instructions.)*

3.  Download the pre-trained YOLOv8 weights (if not already present):
    The code assumes the `yolov8l.pt` weights are in the `yolo_weights` directory. Ensure this file is present, or modify the script to point to its correct location.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

To run the real-time parking lot entry counter from a video file:

1.  Ensure you have a video file (e.g., `cars_ai.mp4`) in the specified location (`../Videos/`).
2.  Ensure you have the mask file (`car_ai_mask.png`) in the specified location (`../Masks/`).
3.  Run the Python script:
    ```sh
    python parking_lot_entry_counter.py
    ```

The application will process the video, display the output with detected and tracked vehicles, the entry line, and the total count of entering vehicles.

You can modify the `VIDEO_SOURCE` variable in your script to use a different video file or even a live webcam feed (if adapted).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Feel free to reach out if you have any questions, suggestions, or would like to collaborate!

* [![Name](https://img.shields.io/badge/Ayush%20Dhanraj-informational?style=for-the-badge)](https://www.linkedin.com/in/ayush-d-1759461a1)
* [![Email](https://img.shields.io/badge/dhanrajaayush123%40gmail.com-important?style=for-the-badge)](mailto:dhanrajaayush123@gmail.com)
* [![Email](https://img.shields.io/badge/ayushdhanraj.work%40gmail.com-important?style=for-the-badge)](mailto:ayushdhanraj.work@gmail.com)
* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-d-1759461a1)
* [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ayush-2001-Dhanraj)

<p align="right">(<a href="#readme-top">back to top</a>)</p>