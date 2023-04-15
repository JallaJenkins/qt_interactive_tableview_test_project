from PyQt5.QtWidgets import (
    QWidget,
    QItemDelegate,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QStyleOptionButton,
    QStyle,
    QCheckBox,
)

from PyQt5.QtCore import Qt, QSize, QModelIndex

# from PyQt5.QtGui import


class CheckBoxDelegate(QStyledItemDelegate):
    def __int__(self):
        super().__init__()

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem',
                     index: QModelIndex) -> QWidget:
        return None

    def paint(self, painter, option, index):
        checked = index.data()
        # self.drawCheck(painter, option, option.rect, Qt.Checked)
        checkbox = QCheckBox()
        checkbox.rect = option.rect
        checkbox.paint(painter, option.rect, option.palette)

    def sizeHint(self):
        return QSize(10, 10)




