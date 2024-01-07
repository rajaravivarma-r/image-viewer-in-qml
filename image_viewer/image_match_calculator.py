import os
import glob

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QThread
from image_match.goldberg import ImageSignature

from . import ImageFile


class ImageMatchCalculator(QThread):
    """
    This is a threaded class, which will find matches for images
    based on the image_match library.import os
    """

    # Emitted when a distinct image file is found
    distinct_image_found = pyqtSignal(
        ImageFile, arguments=["imagePath"], name="distinctImageFileFound"
    )
    # Emitted when a duplicate image is found for another image
    # The first argument will be the original image and the second
    # argument will be the duplicate image.
    duplicate_image_found = pyqtSignal(
        ImageFile,
        ImageFile,
        arguments=["imageFile", "duplicateImageFile"],
        name="imageDuplicatesFound",
    )

    # Emitted when all the duplicate matches are found
    finished = pyqtSignal(object)

    def __init__(self, starting_directory):
        QObject.__init__(self)

        self.starting_directory = starting_directory
        self.glob_path = os.path.join(starting_directory, "*.png")
        self.signature_generator = ImageSignature()
        self.image_files = []
        self.distinct_image_files = []

    def __del__(self):
        self.wait()

    def run(self):
        self.calculate()

    def calculate(self):
        for image_path in glob.iglob(self.glob_path):
            new_image_file = ImageFile(
                path=image_path,
                signature=self._get_image_signatures(image_path),
            )
            original_image = self._find_original_image(new_image_file)
            if original_image:
                self.duplicate_image_found.emit(original_image, new_image_file)
            else:
                self.distinct_image_files.append(new_image_file)
                self.distinct_image_found.emit(new_image_file)

        self.finished.emit(self.distinct_image_files)

    def _find_original_image(self, image):
        for distinct_image in self.distinct_image_files:
            if self._matches(distinct_image, image):
                return distinct_image

    def _matches(self, image_file1, image_file2):
        distance = self.signature_generator.normalized_distance(
            image_file1.signature, image_file2.signature
        )
        return distance <= 0.3

    def _get_image_signatures(self, image_path):
        return self.signature_generator.generate_signature(image_path)

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
            # If this element is None and the previous element is not None,
            # then it must be an ImageFile with all of its duplicates
            # identified
            elif self.image_files[i - 1] is not None:
                self.duplicate_image_found.emit(self.image_files[i - 1])

        self.image_files = [
            image_file
            for image_file in self.image_files
            if image_file is not None
        ]
