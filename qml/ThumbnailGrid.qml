import QtQuick 2.5
import Qt.labs.folderlistmodel 2.11

GridView {
  id: thumbnailGrid
  anchors.fill: parent
  anchors.margins: 10

  cellHeight: 170
  cellWidth: 170

  currentIndex: 1

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
}
