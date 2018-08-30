import QtQuick 2.11

ListView {
    anchors.fill: parent
    model: duplicateImageListModel
    spacing: 2
    delegate: DuplicateImageViewDelegate {}
}
