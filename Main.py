import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit)

from ModeloTabla import ModeloTabla


class TableView(QMainWindow):
    def __init__(self):
        super().__init__()

        super().__init__()
        self.setWindowTitle("Ejemplo de table view")
        self.setFixedSize(400, 400)

        self.datos = [["Nombre", "Dni", "Genero", "Fallecido"],
                      ["Ana perez", "123123123F", "Mujer", False],
                      ["Paco Jémez", "67676767H", "Hombre", True],
                      ["Victor Roque", "12389065H", "Hombre", False],
                      ["Juanita Sainz", "23423423D", "Mujer", True],
                      ["Daniela López", "12345678G", "Otro", False]]



        caja = QVBoxLayout()
        self.tvwTabla = QTableView()
        modelo = ModeloTabla(self.datos)
        self.tvwTabla.setModel(modelo)

        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.cabecera = self.tvwTabla.horizontalHeader()
        cajaHorizontal = QHBoxLayout()
        caja.addLayout(cajaHorizontal)
        self.txtNombre = QLineEdit()
        cajaHorizontal.addWidget(self.txtNombre)

        self.txtDni = QLineEdit()
        cajaHorizontal.addWidget(self.txtDni)
        self.txtGenero = QLineEdit()
        cajaHorizontal.addWidget(self.txtGenero)
        self.txtFallecido = QLineEdit()
        cajaHorizontal.addWidget(self.txtFallecido)


        caja.addWidget(self.tvwTabla)
        container = QWidget()
        container.setLayout(caja)
        self.setCentralWidget(container)
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableView()
    app.exec()




