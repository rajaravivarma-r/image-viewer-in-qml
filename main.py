import sys
import glob

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from image_viewer.image_browser import ImageBrowser
from image_viewer.image_list_model import ImageListModel, ImageFile

if __name__ == "__main__":

    # Create an instance of the application
    app = QGuiApplication(sys.argv)
    # Create QML engine
    engine = QQmlApplicationEngine()

    imageListModel = ImageListModel()
    imageListModel.addImageFile(
        ImageFile(
            path="/Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180707_191723252818.jpg"
        )
    )

    # And register it in the context of QML
    engine.rootContext().setContextProperty("imageListModel", imageListModel)
    # Load the qml file into the engine
    engine.load("qml/main.qml")

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
