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
from image_viewer.image_match_calculator import ImageMatchCalculator


class DuplicateImageListModel(QAbstractListModel):
    class ImageFileRoles(enum.Enum):
        path = Qt.UserRole + 1
        name = path + 1
        duplicates = name + 1

    def __init__(self, parent=None):
        super(DuplicateImageListModel, self).__init__(parent)
        self.imageFiles = []

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if index.row() > len(self.imageFiles):
            return None

        imageFile = self.imageFiles[index.row()]

        if role == Qt.DisplayRole or role == Qt.EditRole:
            return imageFile.name

        if role == DuplicateImageListModel.ImageFileRoles.path.value:
            return imageFile.path

        if role == DuplicateImageListModel.ImageFileRoles.name.value:
            return imageFile.name

        if role == DuplicateImageListModel.ImageFileRoles.duplicates.value:
            return imageFile.duplicates

        return None

    def setData(self, index, value, role):
        pass

    def addImageFile(self, imageFile):
        noOfImageFiles = len(self.imageFiles)
        self.beginInsertRows(QModelIndex(), noOfImageFiles, noOfImageFiles)
        self.imageFiles.append(imageFile)
        self.endInsertRows()

    def roleNames(self):
        return {
            # encode is used because the roleName is expected in byte format
            role.value: role.name.encode()
            for role in DuplicateImageListModel.ImageFileRoles
        }

    def rowCount(self, parent):
        return len(self.imageFiles)

    @pyqtSlot(str)
    def findDuplicateImages(self, imageFolderPath):
        imageMatchCalculator = ImageMatchCalculator(imageFolderPath)
        imageMatchCalculator.image_duplicates_found.connect(self.addImageFile)
        imageMatchCalculator.start()
