from ultralytics import YOLO


model = YOLO('D:/V2_KH_TrafficSign_Detection/runs/detect/traffic_sign_detector2/weights/best.pt')

metrics = model.val()

print(f"mAP50: {metrics.box.map50}")
print(f"mAP50-95: {metrics.box.map}")