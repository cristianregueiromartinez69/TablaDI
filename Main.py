import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout, QLineEdit,
                             QComboBox, QCheckBox, QPushButton, QSizePolicy)

from ModeloTabla import ModeloTabla
from ButtonsCrud import ButtonsCrud
from DatosCrudInterfaz import DatosInterfaz

class TableView(QMainWindow):
    def __init__(self):
        super().__init__()

        super().__init__()
        self.setWindowTitle("Ejemplo de table view")
        self.setFixedSize(800, 400)

        self.datos = [["Nombre", "Dni", "Genero", "Fallecido"],
                      ["Ana perez", "123123123F", "Mujer", False],
                      ["Paco Jémez", "67676767H", "Hombre", True],
                      ["Victor Roque", "12389065H", "Hombre", False],
                      ["Juanita Sainz", "23423423D", "Mujer", True],
                      ["Daniela López", "12345678G", "Otro", False]]



        caja = QHBoxLayout()
        caja_vertical = QVBoxLayout()
        self.tvwTabla = QTableView()
        self.tvwTabla.clicked.connect(self.on_cell_clicked)
        self.modelo = ModeloTabla(self.datos)
        self.tvwTabla.setModel(self.modelo)

        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.cabecera = self.tvwTabla.horizontalHeader()
        cajaHorizontal = QVBoxLayout()

        '''
        otra clase
        '''
        self.datos_crud = DatosInterfaz()
        self.datos_crud.cmb_xenero.addItems(["Mujer", "Hombre", "Otro"])
        cajaHorizontal.addLayout(self.datos_crud)

        self.botonesCrud = ButtonsCrud()
        self.botonesCrud.botton_insertar.clicked.connect(self.on_boton_insert)
        self.botonesCrud.botton_actualizar.clicked.connect(self.on_boton_update)
        self.botonesCrud.botton_borrar.clicked.connect(self.on_boton_delete)

        self.boton_Aceptar = QPushButton("aceptar")
        self.boton_cancelar = QPushButton("cancelar")

        self.boton_cancelar.clicked.connect(self.on_boton_cancelar_clicked)

        self.boton_Aceptar.setStyleSheet("background-color: green;")
        self.boton_cancelar.setStyleSheet("background-color: gray;")

        self.caja_botones_afir_cancel = QHBoxLayout()
        self.caja_botones_afir_cancel.addWidget(self.boton_cancelar)
        self.caja_botones_afir_cancel.addWidget(self.boton_Aceptar)





        caja.addWidget(self.tvwTabla)
        caja_vertical.addLayout(cajaHorizontal)
        caja_vertical.addLayout(self.botonesCrud)
        caja_vertical.addLayout(self.caja_botones_afir_cancel)
        caja.addLayout(caja_vertical)
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
    '''
    Explicacion:
    1. el metodo recibe el indice por parámetro
    2. asignamos una variable al indice que selecciona el usuario
    3. recogemos en una variable la información de la fila asginada
    4. cambiamos los valores de los campos por lo que hay en los datos recogidos
    '''
    def on_cell_clicked(self, index):
        fila = index.row()
        datos_fila = self.modelo.tabla[fila]
        self.txtNombre.setText(datos_fila[0])
        self.txtDni.setText(datos_fila[1])
        self.checkGenero(datos_fila[2])
        self.checkFallecido(datos_fila[3])


    def on_boton_cancelar_clicked(self):
        self.limpiarDatos()


    def on_boton_insert(self):
            if self.txtNombre.text() == "" or self.txtDni.text() == "" or self.cmbGenero.currentIndex() == -1:
                print("Faltan datos para introducir")
            else:
                self.modelo.tabla.append((self.txtNombre.text(), self.txtDni.text(), self.cmbGenero.currentText(), bool(self.chkFallecido.isChecked())))
                self.modelo.layoutChanged.emit()
                self.limpiarDatos()

    def on_boton_delete(self):
        indice = self.tvwTabla.selectedIndexes()
        if indice:
            if self.txtNombre.text() == "" or self.txtDni.text() == "" or self.cmbGenero.currentIndex() == -1:
                print("Faltan datos para introducir")
            else:
                pass

    '''
    Añadir elemento
    1. creamos una variable igual a los indices seleccionados
    2. comprobamos si lo que vamos a actualizar está vacío
    3. si no lo está, actualizamos los datos
    4. IMPORTANTE -> poner el metodo layoutChanged.emit() para que se reflejen los cambios 
    '''
    def on_boton_update(self):
        indice = self.tvwTabla.selectedIndexes()
        if indice:
            if self.txtNombre.text() == "" or self.txtDni.text() == "" or self.cmbGenero.currentIndex() == -1:
                print("Faltan datos para introducir")
            else:
                self.modelo.tabla[indice[0].row()][0] = self.txtNombre.text()
                self.modelo.tabla[indice[0].row()][1] = self.txtDni.text()
                self.modelo.tabla[indice[0].row()][2] = self.cmbGenero.currentText()
                self.modelo.tabla[indice[0].row()][3] = True if self.chkFallecido.isChecked() else False
                self.modelo.layoutChanged.emit()
                self.limpiarDatos()

    def limpiarDatos(self):
        self.txtNombre.clear()
        self.txtDni.clear()
        self.cmbGenero.setCurrentIndex(-1)
        self.chkFallecido.setChecked(False)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableView()
    app.exec()



'''
Hacer que al pulsar en una fila, se manden los datos a los campos de abajo
'''




