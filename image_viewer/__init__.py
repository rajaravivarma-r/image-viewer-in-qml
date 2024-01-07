import os

class ImageFile:
    def __init__(self, path, signature=None, duplicates=None):
        self.path = path
        self.name = os.path.basename(path)
        self.signature = signature
        self.duplicates = duplicates or []
        self.selected = False

    def add_duplicate(self, duplicate_image):
        self.duplicates.append(duplicate_image)

    def set_selection(self, value):
        self.selected = value

    def __repr__(self):
        newline = "\n"
        return (
            f"<Image name: {self.name}, path: {self.path}, "
            f"signature: {self.signature}, selected: {self.selected}>, "
            f"duplicates: {newline.join([img.name for img in self.duplicates])}"
        )
