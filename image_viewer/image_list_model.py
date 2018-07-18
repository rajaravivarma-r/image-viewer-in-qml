import os
import enum

from PyQt5.QtCore import (
    pyqtSlot,
    pyqtSignal,
    QAbstractListModel,
    Qt,
    QModelIndex,
    QByteArray,
)


class ImageFile:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)


class ImageListModel(QAbstractListModel):
    class ImageFileRoles(enum.Enum):
        path = Qt.UserRole + 1
        name = path + 1

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
            role.value: role.name.encode()
            for role in ImageListModel.ImageFileRoles
        }

    def rowCount(self, parent):
        return len(self.imageFiles)
