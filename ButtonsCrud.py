import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit,
                             QComboBox, QCheckBox, QLabel, QPushButton)


class ButtonsCrud(QHBoxLayout):
    def __init__(self):
        super().__init__()
        botton_insertar = QPushButton("insertar")
        botton_actualizar = QPushButton("actualizar")
        botton_borrar = QPushButton("borrar")

        botton_insertar.setStyleSheet("background-color: cyan;")
        botton_actualizar.setStyleSheet("background-color: yellow;")
        botton_borrar.setStyleSheet("background-color: red;")

        self.addWidget(botton_insertar)
        self.addWidget(botton_actualizar)
        self.addWidget(botton_borrar)
