from gui.ui_MainWindow import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from src.APIHandler import get_response
import json



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self._button_clicked)
        self.ui.listWidget.itemClicked.connect(self._recipe_clicked)

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
        html_content = f"""
        <html>
        <head></head>
        <body>
            <h1>{recipe['recipe']['label']}</h1>
            <img src='{imageUrl}' />
            <h2>Ingredients</h2>
            <ul>
        """
        for ingredient in recipe['recipe']['ingredientLines']:
            html_content += f"<li>{ingredient}</li>"
        html_content += f"""
            </ul>
            <a href='{recipe['recipe']['url']}'>Link to recipe</a>
        </body>
        </html>
        """
        self.ui.webEngineView.setHtml(html_content)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
