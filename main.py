import sys
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
import numpy as np
import cv2
from pathlib import Path
import torch
from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes, xyxy2xywh
from utils.plots import Annotator, colors
import uvicorn

app = FastAPI()

class DetectionResult:
    def __init__(self, class_id, class_name, confidence, bbox):
        self.class_id = class_id
        self.class_name = class_name
        self.confidence = confidence
        self.bbox = bbox

@app.post("/detect")
async def detect_objects(image: UploadFile = File(...)):
    # Read the uploaded image file
    image_bytes = await image.read()
    image_pil = Image.open(io.BytesIO(image_bytes))

    # Convert PIL image to OpenCV format and resize
    image_cv = cv2.cvtColor(np.array(image_pil.resize((640, 640))), cv2.COLOR_RGB2BGR)

    print("Image shape:", image_cv.shape)

    # Load the YOLOv5 model
    device = torch.device("cuda") 
    model = load_model(device)

    # Perform object detection
    detections = detect(model, image_cv)

    # Process the detection results
    results = []
    for class_id, confidence, bbox in detections:
        class_name = get_class_name(class_id)
        result = DetectionResult(class_id, class_name, confidence, bbox)
        results.append(result.__dict__)

    # Return the detection results
    return {"detections": results}

def load_model(device):
    # Load the YOLOv5 model
    model = DetectMultiBackend(weights="yolov5s.pt", device=device)
    model.eval()
    return model

def detect(model, image_cv):
    # Preprocess the image
    img = torch.from_numpy(image_cv.transpose(2, 0, 1)).float() / 255.0
    img = img.unsqueeze(0)

    # Perform inference
    with torch.no_grad():
        detections = model(img)

    # Post-process the detections
    detections = non_max_suppression(detections, conf_thres=0.3, iou_thres=0.5)  # Adjust the threshold values

    # Process the detections
    results = []
    for det in detections:
        if det is not None and len(det) > 0:
            det[:, :4] = scale_boxes((image_cv.shape[1], image_cv.shape[0]), det[:, :4], image_cv.shape).round()

            for *xyxy, conf, cls in reversed(det):
                class_id = int(cls)
                confidence = float(conf)
                bbox = [float(xyxy[0]), float(xyxy[1]), float(xyxy[2]), float(xyxy[3])]
                detection = (class_id, confidence, bbox)
                results.append(detection)

    return results


def get_class_name(class_id):
    class_mapping = {
        0: "person",
        1: "bicycle",
        2: "car",
        3: "Trafic Light",
        # Add more class IDs and corresponding object names here
    }
    return class_mapping.get(class_id, "Unknown")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
