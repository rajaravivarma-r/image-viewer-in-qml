import QtQuick 2.11
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.4

ApplicationWindow {
  id: mainWindow
  visible: true
  height: 700
  width: 800

  menuBar: MenuBar {
    Menu {
      title: 'Action'
      MenuItem {
        text: 'Browser'
        onTriggered: {
          duplicateImagesPage.hide()
          thumbnailGrid.show()
        }
      }
      MenuItem {
        text: 'Duplicate Image Browser'
        onTriggered: {
          thumbnailGrid.hide()
          duplicateImagesPage.show()
        }
      }
    }
  }

  header: ToolBar {
    id: topToolBar
    visible: false

    RowLayout {
      anchors.fill: parent

      ToolButton {
        text: 'Delete'
      }
    }
  }

  ThumbnailGrid {
    id: thumbnailGrid
    visible: false

    function show() {
      thumbnailGrid.visible = true
    }

    function hide() {
      thumbnailGrid.visible = false
    }

    Component.onCompleted: {
      console.log('populating images')
      imageListModel.populateImages("/home/raja/Github/image-viewer-in-qml/sample_images")
    }
  }

  DuplicateImagesPage {
    id: duplicateImagesPage
    visible: false

    function show() {
      duplicateImagesPage.visible = true
    }

    function hide() {
      duplicateImagesPage.visible = false
    }

    Component.onCompleted: {
      console.log('finding duplicate images')
      duplicateImageListModel.findDuplicateImages("/home/raja/Github/image-viewer-in-qml/sample_images")
    }
  }
}
