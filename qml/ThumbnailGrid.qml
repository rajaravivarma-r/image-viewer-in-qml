import QtQuick 2.5
import Qt.labs.folderlistmodel 2.11

GridView {
  id: thumbnailGrid
  anchors.fill: parent
  anchors.margins: 10

  cellHeight: 170
  cellWidth: 170

  currentIndex: 1

  FolderListModel {
    id: folderListModel
    nameFilters: ['*.jpg']
    showDirs: false
    showDotAndDotDot: false
    showHidden: false
  }

  delegate: Thumbnail {}
  model: imageListModel

  highlight: Component {
    Rectangle {
      height: thumbnailGrid.cellHeight
      width: thumbnailGrid.cellWidth

      color: 'blue'
      opacity: 0.4
    }
  }
  highlightFollowsCurrentItem: false
  keyNavigationWraps: true
  focus: true

  Component.onCompleted: {
    // folderListModel.folder = 'file:///Users/rajaravivarma/Github/image-viewer/sample_images/'
  }


  // function addImage(imagePath) {
  //   var component;
  //   component = Qt.createComponent("Thumbnail.qml");
  //   console.log('Creating component')

  //   if (component.status == Component.Ready) {
  //     console.log('Component ready')
  //     var thumbnail = component.createObject(thumbnailGrid, {source: imagePath})
  //     if (thumbnail == null) {
  //       console.log('Cannot create thumbnail')
  //     }
  //   }
  //   else {
  //     console.log('Component not ready : ' + component.errorString())
  //   }
  // }
}
