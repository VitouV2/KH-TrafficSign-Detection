from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # nano model (fastest for testing)
# or yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt for larger models

# Train the model
results = model.train(
    data='data.yaml',
    epochs=50,            # Reduce epochs
    imgsz=416,            # Smaller image size (faster)
    batch=4,              # Smaller batch size
    name='traffic_sign_detector',
    patience=20,
    device='cpu',
    workers=4,            # Adjust based on your CPU cores
)