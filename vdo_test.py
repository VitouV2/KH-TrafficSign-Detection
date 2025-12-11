from ultralytics import YOLO
import cv2

model = YOLO('D:/V2_KH_TrafficSign_Detection/runs/detect/traffic_sign_detector/weights/best.pt')

# Run inference on video
results = model('D:/V2_KH_TrafficSign_Detection/Testing4.MP4', save=True)

# Display the results video
video_path = 'runs/detect/predict/TestingVideo.MP4'  # Default output location
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('Traffic Sign Detection', frame)
    
    # Press 'q' to exit the video playback
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()