import QtQuick 2.5

GridView {
  id: thumbnailGrid
  anchors.fill: parent

  cellHeight: 150
  cellWidth: 150

  currentIndex: 1

  delegate: Thumbnail {
    height: cellHeight
    width: cellWidth
  }
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
