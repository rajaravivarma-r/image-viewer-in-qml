import enum

from PyQt5.QtCore import (
    pyqtSlot,
    pyqtSignal,
    QAbstractListModel,
    Qt,
    QModelIndex,
    QByteArray,
)

from . import ImageFile
from image_viewer.image_browser import ImageBrowser


class ImageListModel(QAbstractListModel):
    class ImageFileRoles(enum.Enum):
        path = Qt.UserRole + 1
        name = path + 1
        selected = name + 1

    def __init__(self, parent=None):
        super(ImageListModel, self).__init__(parent)
        self.imageFiles = []

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if index.row() > len(self.imageFiles):
            return None

        imageFile = self.imageFiles[index.row()]

        if role == Qt.DisplayRole or role == Qt.EditRole:
            return imageFile.name

        if role == ImageListModel.ImageFileRoles.path.value:
            return imageFile.path

        if role == ImageListModel.ImageFileRoles.name.value:
            return imageFile.name

        if role == ImageListModel.ImageFileRoles.selected.value:
            return imageFile.selected

        return None

    def setData(self, index, value, role):
        if not index.isValid():
            return False

        if index.row() > len(self.imageFiles):
            return False

        imageFile = self.imageFiles[index.row()]

        if role == ImageListModel.ImageFileRoles.selected.value:
            imageFile.set_selection(value)
            return True

    def addImageFile(self, imageFile):
        noOfImageFiles = len(self.imageFiles)
        self.beginInsertRows(QModelIndex(), noOfImageFiles, noOfImageFiles)
        self.imageFiles.append(imageFile)
        self.endInsertRows()

    def roleNames(self):
        return {
            # encode is used because the roleName is expected in byte format
            role.value: role.name.encode()
            for role in ImageListModel.ImageFileRoles
        }

    def rowCount(self, parent):
        return len(self.imageFiles)

    @pyqtSlot(str)
    def populateImages(self, imageFolderPath):
        imageBrowser = ImageBrowser(imageFolderPath)
        imageBrowser.imageFileDetected.connect(
            lambda imagePath: self.addImageFile(ImageFile(imagePath))
        )
        imageBrowser.start()
