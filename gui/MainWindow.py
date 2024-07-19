from gui.ui_MainWindow import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from src.APIHandler import get_response
import json
from src.HTML import to_HTML



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self._button_clicked)
        self.ui.listWidget.itemClicked.connect(self._recipe_clicked)

        css = """
        QWidget {
            background-color: #f0f0f0;
            color: #333;
            border: 1px solid #000;
            border-radius: 5px;
        }
        """
        self.setStyleSheet(css)

    def _button_clicked(self):
        self.ui.listWidget.clear()
        self._load_recipes()

    def _load_recipes(self):
        query = self.ui.textEdit.toPlainText()
        get_response(query)
        with open('data/recipes.json') as f:
            data = json.load(f)
            for recipe in data['hits']:
                item = QListWidgetItem()
                item.setText(recipe['recipe']['label'])
                item.setData(Qt.UserRole, recipe)
                self.ui.listWidget.addItem(item)

    def _recipe_clicked(self):
        item = self.ui.listWidget.currentItem()
        recipe = item.data(Qt.UserRole)
        imageUrl = recipe['recipe']['image']
        
        html_content = to_HTML(recipe)
        self.ui.webEngineView.setHtml(html_content)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
