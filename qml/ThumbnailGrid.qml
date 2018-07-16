import QtQuick 2.5

Item {
  Grid {
    id: thumbnailGrid
    columns: 3
    anchors.fill: parent
    spacing: 6
  }

  function addImage(imagePath) {
    var component;
    component = Qt.createComponent("Thumbnail.qml");
    console.log('Creating component')

    if (component.status == Component.Ready) {
      console.log('Component ready')
      var thumbnail = component.createObject(thumbnailGrid, {source: imagePath})
      if (thumbnail == null) {
        console.log('Cannot create thumbnail')
      }
    }
    else {
      console.log('Component not ready : ' + component.errorString())
    }
  }
}
