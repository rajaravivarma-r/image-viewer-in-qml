import QtQuick 2.11

Item {
  id: thumbnailContainer

  CheckBox {
    anchors.right: thumbnailContainer.right
    anchors.top: thumbnailContainer.top
    anchors.rightMargin: 1
    anchors.topMargin: 2
    z: 1

    onCheckStateChanged: {
      if (checkState == Qt.Checked) {
        selected = true
      }
      else if (checkState == Qt.Unchecked) {
        selected = false
      }
    }
  }

  Image {
    id: image
    autoTransform: true
    anchors.fill: parent

    anchors.leftMargin: getLeftMargin()
    anchors.topMargin: getTopMargin()

    asynchronous: true
    sourceSize.height: height
    sourceSize.width: width
    clip: true
    source: path
    fillMode: Image.PreserveAspectCrop
  }

  function getLeftMargin() {
    if (thumbnailContainer.GridView.view === null) {
      return 0;
    }

    if (thumbnailContainer.x === thumbnailContainer.GridView.view.x) {
      return 0;
    }
    else {
      return 2;
    }
  }

  function getTopMargin() {
    if (thumbnailContainer.GridView.view === null) {
      return 0;
    }

    if (thumbnailContainer.y === thumbnailContainer.GridView.view.y) {
      return 0;
    }
    else {
      return 2;
    }
  }
}
