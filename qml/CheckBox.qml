import QtQuick 2.11
import QtQuick.Controls 2.4

CheckBox {
  id: control
  checked: false
  opacity: 0.4

  indicator: Rectangle {
    implicitWidth: 26
    implicitHeight: 26
    x: control.leftPadding
    y: parent.height / 2 - height / 2
    radius: 3
    border.color: control.down ? "#17a81a" : "#21be2b"

    Rectangle {
      width: 14
      height: 14
      anchors.centerIn: parent
      radius: 2
      color: control.down ? "#17a81a" : "#21be2b"
      visible: control.checked
    }
  }
}
