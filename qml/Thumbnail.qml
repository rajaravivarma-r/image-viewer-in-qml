import QtQuick 2.5

Item {
  Image {
    height: 150
    width:  150
    anchors.margins: 10
    autoTransform: true
    asynchronous: true
    sourceSize.width: 150
    sourceSize.height: 150
    clip: true
    source: path
  }
}
