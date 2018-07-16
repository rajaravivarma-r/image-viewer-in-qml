import os
import glob
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class ImageBrowser(QObject):
    # Emitted when an image file is detected in the path
    image_file_detected = pyqtSignal(
        str, arguments=["imagePath"], name="imageFileDetected"
    )

    def __init__(self, starting_directory):
        QObject.__init__(self)

        self.starting_directory = starting_directory
        self.glob_path = os.path.join(starting_directory, "**", "*.jpg")

    @pyqtSlot()
    def browse(self):
        for image_path in glob.iglob(self.glob_path):
            self.image_file_detected.emit(image_path)
