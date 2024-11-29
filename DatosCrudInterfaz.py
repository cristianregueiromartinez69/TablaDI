import sys
from tkinter import Checkbutton

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit,
                             QComboBox, QCheckBox, QPushButton, QLabel)

from ModeloTabla import ModeloTabla
from ButtonsCrud import ButtonsCrud

class DatosInterfaz(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.nome_xenero_caha_h = QHBoxLayout()
        self.nome_xenero_caha_h.setSpacing(10)
        self.nome_xenero_caha_h.setContentsMargins(10, 10, 10, 10)
        self.dni_fallecido_caha_h = QHBoxLayout()
        self.dni_fallecido_caha_h.setSpacing(10)
        self.dni_fallecido_caha_h.setContentsMargins(10, 10, 10, 10)

        self.label_nombre = QLabel("Nombre")
        self.text_nombre = QLineEdit()
        self.text_nombre.setFixedSize(150,30)


        self.label_xenero = QLabel("Xenero")
        self.cmb_xenero = QComboBox()

        self.label_dni = QLabel("DNI")
        self.text_dni = QLineEdit()
        self.text_dni.setContentsMargins(0,0,90,0)
        self.text_dni.setFixedSize(215,30)

        self.boton_fallecido = QCheckBox("Fallecido")

        self.nome_xenero_caha_h.addWidget(self.label_nombre)
        self.nome_xenero_caha_h.addWidget(self.text_nombre)
        self.nome_xenero_caha_h.addWidget(self.label_xenero)
        self.nome_xenero_caha_h.addWidget(self.cmb_xenero)

        self.dni_fallecido_caha_h.addWidget(self.label_dni)
        self.dni_fallecido_caha_h.addWidget(self.text_dni)
        self.dni_fallecido_caha_h.addWidget(self.boton_fallecido)

        self.caja_principal = QVBoxLayout()

        self.addLayout(self.nome_xenero_caha_h)
        self.addLayout(self.dni_fallecido_caha_h)


