import QtQuick 2.5

Item {
  id: thumbnailContainer

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
