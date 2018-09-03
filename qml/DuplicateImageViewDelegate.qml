import QtQuick 2.11
import QtQuick.Layouts 1.11

Item {
  id: duplicateImageViewDelegate
  anchors.left: parent.left
  anchors.right: parent.right
  height: columnLayout.childrenRect.height

  ColumnLayout {
    id: columnLayout
    spacing: 0
    anchors.fill: parent

    Image {
      source: path
      autoTransform: true
      Layout.preferredWidth: duplicateImageViewDelegate.width
      Layout.preferredHeight: 200
      Layout.alignment: Qt.AlignVCenter

      sourceSize.width: width
      sourceSize.height: height

      fillMode: Image.PreserveAspectFit
    }

    GridLayout {
      id: duplicateImageGrid
      Layout.fillWidth: true
      Layout.fillHeight: true

      columns: 4

      Repeater {
        model: duplicates

        Item {
          Layout.preferredWidth: 150
          Layout.preferredHeight: 100
          Layout.fillWidth: true

          Image {
            anchors.fill: parent
            anchors.leftMargin: 1
            anchors.topMargin: 1

            autoTransform: true

            sourceSize.width: height
            sourceSize.height: width

            clip: true
            source: path
            fillMode: Image.PreserveAspectFit
          }
        }
      }
    }
  }
}
