import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit,
                             QComboBox, QCheckBox)

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
        self.tvwTabla.clicked.connect(self.on_cell_clicked)
        modelo = ModeloTabla(self.datos)
        self.tvwTabla.setModel(modelo)

        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.cabecera = self.tvwTabla.horizontalHeader()
        cajaHorizontal = QHBoxLayout()
        self.txtNombre = QLineEdit()
        cajaHorizontal.addWidget(self.txtNombre)

        self.txtDni = QLineEdit()
        cajaHorizontal.addWidget(self.txtDni)
        self.cmbGenero = QComboBox()
        self.cmbGenero.addItems(["Mujer", "Hombre", "Otro"])

        cajaHorizontal.addWidget(self.cmbGenero)

        self.chkFallecido = QCheckBox("Fallecido")
        cajaHorizontal.addWidget(self.chkFallecido)



        caja.addWidget(self.tvwTabla)
        caja.addLayout(cajaHorizontal)
        container = QWidget()
        container.setLayout(caja)
        self.setCentralWidget(container)
        self.show()




    def checkGenero(self, genero):
        if genero == "Mujer":
            self.cmbGenero.setCurrentIndex(0)
        elif genero == "Hombre":
            self.cmbGenero.setCurrentIndex(1)
        else:
            self.cmbGenero.setCurrentIndex(2)

    def checkFallecido(self, estado):
        if estado:
            self.chkFallecido.setChecked(True)
        else:
            self.chkFallecido.setChecked(False)


    def on_cell_clicked(self, index):
        fila = index.row()
        datos_fila = self.datos[fila]

        self.txtNombre.setText(datos_fila[0])
        self.txtDni.setText(datos_fila[1])
        self.checkGenero(datos_fila[2])
        self.checkFallecido(datos_fila[3])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableView()
    app.exec()



'''
Hacer que al pulsar en una fila, se manden los datos a los campos de abajo
'''




