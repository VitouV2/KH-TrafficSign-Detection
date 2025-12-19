import gradio as gr
from ultralytics import YOLO

# 1. Load the Model (Only once)
model = YOLO('D:/V2_KH_TrafficSign_Detection/runs/detect/traffic_sign_detector/weights/best.pt')

# 2. Define the prediction function
def detect_traffic_signs(image):
    # The Gradio interface will pass the image to this function
    # The model will run inference and return the image with annotations
    results = model.predict(source=image)
    # The .plot() method returns the image with boxes drawn
    return results[0].plot()

# 3. Create the Gradio Interface
# Define inputs (image upload) and outputs (annotated image)
gr.Interface(
    fn=detect_traffic_signs,
    inputs=gr.Image(type="filepath", label="Upload Image"),
    outputs=gr.Image(label="Detection Results"),
    title="Traffic Sign Detection (YOLOv8 Demo)",
    description="Upload an image to see the model detect traffic signs."
).launch()