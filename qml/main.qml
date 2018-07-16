import QtQuick 2.5
import QtQuick.Controls 1.4

ApplicationWindow {
  id: mainWindow
  visible: true
  height: 700
  width: 800

  ThumbnailGrid {
    id: thumbnailGrid
    anchors.fill: parent
  }

  Connections {
    target: imageBrowser
    onImageFileDetected: {
      thumbnailGrid.addImage(imagePath)
    }
  }

  Component.onCompleted: {
    imageBrowser.browse()
  }
}


