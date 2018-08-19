import QtQuick 2.11

ListView {
    anchors.fill: parent
    model: duplicateImageListModel
    delegate: DuplicateImageViewDelegate {}
}
