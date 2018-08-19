import QtQuick 2.11

Item {
  id: duplicateImageViewDelegate
  anchors.left: parent.left
  anchors.right: parent.right
  height: 200

  Column {
    Image {
      source: path
      autoTransform: true
      width: duplicateImageViewDelegate.width
      height: 100

      sourceSize.width: width
      sourceSize.height: height
    }

    ListView {
      id: listView
      anchors.left: parent.left
      anchors.right: parent.right
      height: 100

      orientation: Qt.Horizontal
      layoutDirection: Qt.LeftToRight

      model: duplicates

      delegate: Item {
        width: 150
        height: 100

        Image {
          anchors.fill: parent
          anchors.margins: 10

          autoTransform: true

          sourceSize.width: height
          sourceSize.height: width

          clip: true
          source: path
        }
      }
    }
  }

}
