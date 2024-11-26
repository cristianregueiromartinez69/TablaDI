import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit,
                             QComboBox, QCheckBox, QLabel, QPushButton)


class ButtonsCrud(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.botton_insertar = QPushButton("insertar")
        self.botton_actualizar = QPushButton("actualizar")
        self.botton_borrar = QPushButton("borrar")

        self.botton_insertar.setStyleSheet("background-color: cyan;")
        self.botton_actualizar.setStyleSheet("background-color: yellow;")
        self.botton_borrar.setStyleSheet("background-color: red;")

        self.addWidget(self.botton_insertar)
        self.addWidget(self.botton_actualizar)
        self.addWidget(self.botton_borrar)
