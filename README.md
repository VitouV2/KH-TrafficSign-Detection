# 🇰🇭 Traffic Sign Detection (YOLOv8)

## 💡 Overview
This repository contains the code and weights for a custom-trained YOLOv8 object detection model designed to identify specific Khmer traffic signs.

* **Task:** Khmer Traffic Sign Detection
* **Model:** YOLOv8n (trained on custom dataset)
* **Dataset:** [Khmer-Traffic-sign](https://github.com/VitouV2/Khmer-Traffic-sign)
* **Best Model Weights:** [`runs/detect/traffic_sign_detector/weights/best.pt`](./runs/detect/traffic_sign_detector/weights/best.pt)
* **Classes:** 13 traffic sign types (see [data.yaml](./data.yaml) for details)

## 🚀 Usage

### 1. Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VitouV2/KH-TrafficSign-Detection.git
   cd KH-TrafficSign-Detection
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 2. Running the Model

#### Web App (Gradio)
Run the interactive web app for image upload and detection:
```bash
python app.py
```
Then open the provided URL in your browser.

#### Live Webcam Prediction
Run prediction on your webcam feed:
```bash
python predict.py
```

#### Video Prediction
Run prediction on a video file (e.g., Testing4.mp4):
```bash
python vdo_test.py
```
The processed video will be saved in `runs/detect/predict/` and displayed.

#### Image/Video Prediction (CLI)
Use the Ultralytics CLI for custom inputs:
```bash
yolo predict model=runs/detect/traffic_sign_detector/weights/best.pt source=path/to/your/input conf=0.25
```
Replace `path/to/your/input` with an image, video, or directory.

#### Evaluation
Evaluate the model on the validation set:
```bash
python evaluate.py
```

#### Training (Optional)
To retrain the model (requires dataset):
```bash
python train.py
```

## 📁 Project Structure
- `app.py`: Gradio web app for image detection
- `predict.py`: Live webcam prediction
- `vdo_test.py`: Video file prediction
- `evaluate.py`: Model evaluation script
- `train.py`: Training script
- `data.yaml`: Dataset configuration
- `yolov8n.pt`: Base YOLOv8n model
- `runs/detect/traffic_sign_detector/weights/best.pt`: Trained model weights
- `requirements.txt`: Python dependencies

## 📊 Model Performance
- Trained for 20-50 epochs on custom dataset
- Optimized for 13 Khmer traffic sign classes
- Best weights available for immediate use

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements.

## 📄 License
This project is open-source. Please check the dataset repository for any licensing details.
