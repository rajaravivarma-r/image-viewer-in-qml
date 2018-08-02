import os


class ImageFile:
    def __init__(self, path, signature=None, duplicates=None):
        self.path = path
        self.name = os.path.basename(path)
        self.signature = signature
        self.duplicates = duplicates or []

    def add_duplicate(self, duplicate_image):
        self.duplicates.append(duplicate_image)
