from PyQt5.QtWidgets import QWidget, QTableView, QCheckBox, QAbstractItemView
from PyQt5.QtCore import Qt, QAbstractItemModel, QAbstractTableModel

# from delegates import CheckBoxDelegate

saves_data = [
    [False, "Strength", 0],
    [False, "Dexterity", 0],
    [False, "Constitution", 0],
    [False, "Intelligence", 0],
    [False, "Wisdom", 0],
    [False, "Charisma", 0],
]


class TestModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def data(self, index, role):
        value = self.data[index.row()][index.column()]

        if role == Qt.DisplayRole:

            if index.column() == 0:
                # return RadioButtonDelegate()
                # if isinstance(value, bool):
                #     return "T" if value is True else "F"
                # else:
                return ""

            if index.column() == 1:
                return value

            if index.column() == 2:
                return value

        if role == Qt.TextAlignmentRole:
            if index.column() == 2:
                return Qt.AlignCenter

    def rowCount(self, index):
        return len(self.data)

    def columnCount(self, index):
        return len(self.data[0])

    def update_modifier_data(self):
        print("Update saves_data called")
        for row in saves_data:
            row[2] = int(row[0])
        print(saves_data)
        self.update_saves_view()

    def update_saves_view(self):
        index1 = self.index(0, 0)
        index2 = self.index(len(self.data), len(self.data[0]))
        self.dataChanged.emit(index1, index2)


class TestView(QTableView):
    def __init__(self):
        super(TestView, self).__init__()

        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.setShowGrid(False)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        # self.setItemDelegateForColumn(0, CheckBoxDelegate())


class TestCheckBox(QCheckBox):
    def __init__(self, model, row):
        super().__init__()

        self.row = row
        self.model = model

    # def __init__(self):
    #     super().__init__()

    def checkbox_clicked(self, state):
        saves_data[self.row][0] = bool(state)
        self.model.update_modifier_data()












