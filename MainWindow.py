from ui_MainWindow import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from APIHandler import get_response
import json



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self._button_clicked)

    def _button_clicked(self):
        self.ui.listWidget.clear()
        self._load_recipes()

    def _load_recipes(self):
        query = self.ui.textEdit.toPlainText()
        get_response(query)
        with open('recipes.json') as f:
            data = json.load(f)
            for recipe in data['hits']:
                item = QListWidgetItem()
                item.setText(recipe['recipe']['label'])
                item.setData(Qt.UserRole, recipe)
                self.ui.listWidget.addItem(item)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
