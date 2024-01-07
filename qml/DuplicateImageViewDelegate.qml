import QtQuick 2.11
import QtQuick.Layouts 1.11

Item {
  id: duplicateImageViewDelegate
  anchors.left: parent.left
  anchors.right: parent.right
  height: columnLayout.childrenRect.height
  // property var modelPath: model.path
  property var modelDuplicates: duplicates

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
      // Component.onCompleted: { 
      //   console.log(duplicates) 
      //   var duplicate = duplicates[0]
      //   if (duplicate !== null) {
      //     console.log(duplicate.path)
      //   }
      // }
    }

    GridLayout {
      id: duplicateImageGrid
      Layout.fillWidth: true
      Layout.fillHeight: true
      rowSpacing: 1

      columns: duplicates.length > 4 ? 4 : duplicates.length

      Repeater {
        id: duplicateRepeater
        model: duplicateImageViewDelegate.modelDuplicates

        Image {
          // anchors.fill: parent
          // anchors.leftMargin: 1
          // anchors.topMargin: 1

          Layout.preferredWidth: 150
          Layout.preferredHeight: 100
          Layout.fillWidth: true

          autoTransform: true

          sourceSize.width: height
          sourceSize.height: width

          clip: true
          source: modelData
          fillMode: Image.PreserveAspectFit
          Component.onCompleted: { 
            // console.log('Original path: ', duplicateImageViewDelegate.modelPath) 
            // console.log('modelData path: ', path) 
            // console.log('duplicates: ', modelData) 
            // if (!duplicateImageViewDelegate.modelDuplicates) { return }

            // for (var i = 0; i < duplicateImageViewDelegate.modelDuplicates.length; i++) {
            //   console.log('Duplicate path: ', duplicateImageViewDelegate.modelDuplicates[i]) 
            // }
          }
        }
      }
    }
  }
}
