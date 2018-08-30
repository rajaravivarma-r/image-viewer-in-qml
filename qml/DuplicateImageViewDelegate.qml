import QtQuick 2.11
import QtQuick.Layouts 1.11

Item {
  id: duplicateImageViewDelegate
  anchors.left: parent.left
  anchors.right: parent.right
  height: 200

  ColumnLayout {
    spacing: 0

    Image {
      source: path
      autoTransform: true
      Layout.preferredWidth: duplicateImageViewDelegate.width
      Layout.preferredHeight: 100
      Layout.alignment: Qt.AlignVCenter

      sourceSize.width: width
      sourceSize.height: height

      fillMode: Image.PreserveAspectFit
    }

    ListView {
      id: listView
      Layout.preferredHeight: 100
      Layout.preferredWidth: duplicateImageViewDelegate.width
      Layout.alignment: Qt.AlignVCenter

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
