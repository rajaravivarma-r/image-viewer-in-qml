import QtQuick 2.11
import QtQuick.Layouts 1.11

Rectangle {
  id: root
  width: 440
  height: 600
  color: 'yellow'

  Flow {
    id: imageGrid
    anchors.fill: root

    Image {
      source: "file:///Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_125730164.jpg"
      height: 200
      sourceSize.width: width
      sourceSize.height: height
      autoTransform: true
      fillMode: Image.PreserveAspectFit
    }

    Image {
      source: "file:///Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180901_130031395_PORTRAIT.jpg"
      height: 200
      sourceSize.width: width
      sourceSize.height: height
      autoTransform: true
      fillMode: Image.PreserveAspectFit
    }

    Image {
      source: "file:///Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180902_190015430.jpg"
      height: 200
      sourceSize.width: width
      sourceSize.height: height
      autoTransform: true
      fillMode: Image.PreserveAspectFit
    }


    Image {
      source: "file:///Users/rajaravivarma/Github/image-viewer/sample_images/IMG_20180902_190110905.jpg"
      height: 200
      sourceSize.width: width
      sourceSize.height: height
      autoTransform: true
      fillMode: Image.PreserveAspectFit
    }
  }
}
