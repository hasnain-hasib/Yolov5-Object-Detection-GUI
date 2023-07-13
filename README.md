
# Object Detection GUI

```
# Object Detection GUI

This is a graphical user interface (GUI) application for object detection using YOLOv5. It allows you to select an image, send it to a FastAPI app for object detection, and display the annotated image with bounding boxes and class labels.

## Prerequisites

- Python 3.6 or later
- PyQt5
- requests
- Pillow
- OpenCV
- PyTorch
- YOLOv5
- uvicorn
- FastAPI

## Installation

1. Clone the repository:



2. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Start the FastAPI app:

   ```
   uvicorn main:app --reload
   ```

4. Run the GUI application:

   ```
   python gui.py
   ```

## Usage

1. Launch the GUI application by running `python gui.py`.

2. Click the "Detect" button to open a file dialog.

3. Select an image file to perform object detection.

4. The GUI will display the annotated image with bounding boxes and class labels.

5. You can click the "Exit" button to close the application.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.







