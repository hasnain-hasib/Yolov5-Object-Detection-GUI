import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt

class MyGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Object Detection")
        self.setGeometry(100, 100, 800, 600)  # Increase the window size

        self.detect_button = QPushButton("Detect", self)
        self.detect_button.setGeometry(350, 500, 100, 30)  # Adjust the position of the Detect button
        self.detect_button.clicked.connect(self.detect_button_clicked)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 50, 700, 400)  # Increase the size of the image label
        self.image_label.setAlignment(Qt.AlignCenter)  # Center the image label

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(350, 550, 100, 30)  # Adjust the position of the Exit button
        self.exit_button.clicked.connect(self.exit_button_clicked)

    def detect_button_clicked(self):
        # Open a file dialog to select the image file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.jpg *.png)", options=options)

        if image_path:
            # Read the selected image file
            with open(image_path, "rb") as file:
                image_data = file.read()

            # Send a POST request to your FastAPI app for object detection
            response = requests.post("http://localhost:8000/detect", files={"image": image_data})

            if response.status_code == 200:
                # Process the detection results here
                data = response.json()
                detections = data["detections"]

                # Load the original image
                pixmap = QPixmap(image_path)

                # Create a QPainter object to draw on the pixmap
                painter = QPainter(pixmap)
                painter.setPen(QPen(QColor(255, 0, 0), 2))  # Set pen color to red and line thickness to 2

                # Draw bounding boxes on the image
                for detection in detections:
                    bbox = detection["bbox"]
                    class_name = detection["class_name"]
                    x, y, w, h = map(int, bbox)  # Convert the coordinates to integers
                    painter.drawRect(x, y, w, h)
                    painter.drawText(x, y - 10, class_name)  # Display the class name above the bounding box

                painter.end()

                # Update the image label with the annotated image
                self.image_label.setPixmap(pixmap.scaled(700, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                print("Detection failed")

    def exit_button_clicked(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    my_gui = MyGUI()
    my_gui.show()

    sys.exit(app.exec_())
