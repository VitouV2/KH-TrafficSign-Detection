# 🇰🇭 Traffic Sign Detection (YOLOv8)

## 💡 Overview
This repository contains the code and weights for a custom-trained YOLOv8 object detection model designed to identify specific traffic signs.

* **Task:** Object Detection
* **Model:** YOLOv8s (or whichever base model you used)
* **Dataset:** [(https://github.com/VitouV2/Khmer-Traffic-sign)]
* **Best Model Weights:** [`runs/detect/traffic_sign_detector/weights/best.pt`](./runs/detect/traffic_sign_detector/weights/best.pt)

## 🚀 Usage

### 1. Installation

1.  **Clone the repository:**
    ```bash
    git clone YOUR_HTTPS_URL_HERE
    cd KH-TrafficSign-Detection
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # Linux/macOS
    ```

3.  **Install dependencies:**
    (You should have created a `requirements.txt` file in the previous steps)
    ```bash
    pip install -r requirements.txt
    ```

### 2. Running the Trained Model (Prediction)

You can run the model on images, video files, or a live webcam feed using the Ultralytics CLI.
Run Predict.py for live cam
or vdo_test.py for Video
and evaluate.py for test image

#### A. On a Single Image/Video

Replace `path/to/your/input` with the file or folder you want to test.
```bash
yolo predict \
  model=runs/detect/traffic_sign_detector/weights/best.pt \
  source=path/to/your/input \
  conf=0.25  # Optional: adjust confidence threshold
