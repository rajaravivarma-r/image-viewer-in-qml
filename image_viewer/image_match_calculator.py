import glob

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from image_match.goldberg import ImageSignature

from .image_list_model import ImageFile


class ImageMatchCalculator(QThread):
    """
    This is a threaded class, which will find matches for images
    based on the image_match library.import os
    """

    # Emitted when image file signature is calculated successfully
    image_signature_calculated = pyqtSignal(
        str, arguments=["imagePath"], name="imageProcessed"
    )
    # Emitted when all the duplicate matches are found
    finished = pyqtSignal(object)

    def __init__(self, starting_directory):
        QObject.__init__(self)

        self.starting_directory = starting_directory
        self.glob_path = os.path.join(starting_directory, "*.jpg")
        self.signature_generator = ImageSignature()
        self.image_files = []

    def __del__(self):
        self.wait()

    def run(self):
        self.calculate()

    def calculate(self):
        for image_path in glob.iglob(self.glob_path):
            self.image_files.append(
                ImageFile(
                    path=image_path,
                    signature=self._get_image_signatures(image_path),
                )
            )
            self.image_signature_calculated.emit(image_path)

        self._compute_matches()
        self.finished.emit(self.image_files)

    def _compute_matches(self):
        for i in range(len(self.image_files)):
            image_file = self.image_files[i]

            if image_file is not None:
                for j in range(i + 1, len(self.image_files)):
                    another_image_file = self.image_files[j]

                    if another_image_file is not None:
                        if self._matches(image_file, another_image_file):
                            image_file.add_duplicate(another_image_file)
                            self.image_files[j] = None

        self.image_files = [
            image_file
            for image_file in self.image_files
            if image_file is not None
        ]

    def _matches(self, image_file1, image_file2):
        distance = self.signature_generator.normalized_distance(
            image_file1.signature, image_file2.signature
        )
        print(
            f"Distance between {image_file1.name} and {image_file2.name}: "
            f"{distance}"
        )
        return distance <= 0.3

    def _get_image_signatures(self, image_path):
        return self.signature_generator.generate_signature(image_path)
