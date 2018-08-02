import QtQuick 2.5

ListView {
    anchors.fill: parent
    model: duplicateImageListModel
    delegate: DuplicateImageViewDelegate {}
}
