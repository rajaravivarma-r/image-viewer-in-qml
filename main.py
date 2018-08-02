import sys
import glob

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from image_viewer.image_list_model import ImageListModel
from image_viewer.duplicate_image_list_model import DuplicateImageListModel


if __name__ == "__main__":

    # Create an instance of the application
    app = QGuiApplication(sys.argv)
    # Create QML engine
    engine = QQmlApplicationEngine()

    imageListModel = ImageListModel()
    duplicateImageListModel = DuplicateImageListModel()
    # And register it in the context of QML
    engine.rootContext().setContextProperty("imageListModel", imageListModel)
    engine.rootContext().setContextProperty(
        "duplicateImageListModel", duplicateImageListModel
    )
    # Load the qml file into the engine
    engine.load("qml/main.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
