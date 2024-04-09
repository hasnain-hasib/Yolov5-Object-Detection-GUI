# Object Detection GUI with FastAPI Backend (Ubuntu 20.04)

This project combines a PyQt5 GUI application for object detection with a FastAPI backend for inference, running on Ubuntu 20.04. The GUI allows users to select an image file and perform object detection using a pre-trained YOLOv5 model. The detected objects are displayed with bounding boxes and class labels on the original image.

## Prerequisites

Before running the project on your Ubuntu 20.04 system, make sure you have the following prerequisites installed:

- Python 3.x
- PyQt5 (`pip install PyQt5`)
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- FastAPI (`pip install fastapi`)
- Uvicorn (`pip install uvicorn`)
- PyTorch (`pip install torch torchvision`)
- Requests (`pip install requests`)

## Usage

1. Run the FastAPI backend by executing the `main.py` script:
2. Run the PyQt5 GUI application by executing the `gui.py` script:
3. Click the "Detect" button in the GUI window to select an image file for object detection.
4. Once the detection is complete, the GUI will display the annotated image with bounding boxes and class labels.
5. Click the "Exit" button to close the application.

## Components

### GUI (gui.py)

- The PyQt5 GUI application provides a simple interface for selecting an image file and displaying the detection results.
- Users can click the "Detect" button to open a file dialog and select an image for object detection.
- The detected objects are displayed with bounding boxes and class labels on the original image.
- The "Exit" button closes the application.

### FastAPI Backend (main.py)

- The FastAPI backend serves as the inference engine for object detection.
- It receives image files via POST requests and returns the detection results in JSON format.
- The uploaded image is preprocessed, and object detection is performed using a pre-trained YOLOv5 model.
- The detection results are processed and returned to the GUI application.

## Acknowledgments

- This project utilizes PyQt5 for the GUI development and FastAPI for the backend implementation.
- Special thanks to the authors of YOLOv5 for providing the object detection model.

## References

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [YOLOv5 GitHub Repository](https://github.com/ultralytics/yolov5)

Feel free to modify and extend this project according to your requirements! If you have any questions or suggestions, please feel free to reach out.
