from ultralytics import YOLO

model = YOLO('D:/V2_KH_TrafficSign_Detection/runs/detect/traffic_sign_detector/weights/best.pt')

model.predict(source=1  , show=True, stream=True)