import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, QTableView, QHBoxLayout,
                             QPushButton)

from ModeloTabla import ModeloTabla
from ButtonsCrud import ButtonsCrud
from DatosCrudInterfaz import DatosInterfaz
from ConexionDB import ConexionBD

class TableView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de table view")
        self.setFixedSize(860, 400)

        # Conexión a la base de datos
        self.base = ConexionBD("usuarios.db")
        self.base.crear_tabla()
        #self.base.insertar_datos_iniciales()
        self.datos = self.base.consultaSenParametros("SELECT * FROM usuarios")

        # Layouts y configuración de la tabla
        caja = QHBoxLayout()
        caja_vertical = QVBoxLayout()
        self.tvwTabla = QTableView()
        self.tvwTabla.clicked.connect(self.on_cell_clicked)

        # Modelo de datos
        self.modelo = ModeloTabla(self.datos) if self.datos else ModeloTabla()
        self.tvwTabla.setModel(self.modelo)
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.cabecera = self.tvwTabla.horizontalHeader()


        # Resto de la interfaz
        cajaHorizontal = QVBoxLayout()
        self.datos_crud = DatosInterfaz()
        self.datos_crud.cmb_xenero.addItems(["Mujer", "Hombre", "Otro"])
        cajaHorizontal.addLayout(self.datos_crud)

        self.botonesCrud = ButtonsCrud()
        self.botonesCrud.botton_insertar.clicked.connect(self.on_boton_insert)
        self.botonesCrud.botton_actualizar.clicked.connect(self.on_boton_update)
        self.botonesCrud.botton_borrar.clicked.connect(self.on_boton_delete)

        # Botones aceptar/cancelar
        self.boton_Aceptar = QPushButton("Aceptar")
        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_cancelar.clicked.connect(self.on_boton_cancelar_clicked)
        self.boton_Aceptar.setStyleSheet("background-color: green;")
        self.boton_cancelar.setStyleSheet("background-color: gray;")
        self.caja_botones_afir_cancel = QHBoxLayout()
        self.caja_botones_afir_cancel.addWidget(self.boton_cancelar)
        self.caja_botones_afir_cancel.addWidget(self.boton_Aceptar)

        # Configuración final
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
            self.datos_crud.cmb_xenero.setCurrentIndex(0)
        elif genero == "Hombre":
            self.datos_crud.cmb_xenero.setCurrentIndex(1)
        else:
            self.datos_crud.cmb_xenero.setCurrentIndex(2)

    def checkFallecido(self, estado):
        if estado:
            self.datos_crud.boton_fallecido.setChecked(True)
        else:
            self.datos_crud.boton_fallecido.setChecked(False)
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
        self.datos_crud.text_nombre.setText(datos_fila[0])
        self.datos_crud.text_dni.setText(datos_fila[1])
        self.checkGenero(datos_fila[2])
        self.checkFallecido(datos_fila[3])


    def on_boton_cancelar_clicked(self):
        self.limpiarDatos()


    def on_boton_insert(self):
            if self.datos_crud.text_nombre.text() == "" or self.datos_crud.text_dni.text() == "" or self.datos_crud.cmb_xenero.currentIndex() == -1:
                print("Faltan datos para introducir")
            else:
                nuevo_usuario = (
                    self.datos_crud.text_dni.text(),
                    self.datos_crud.text_nombre.text(),
                    self.datos_crud.cmb_xenero.currentText(),
                    int(self.datos_crud.boton_fallecido.isChecked()),
                )

                # Inserta en la base de datos
                self.base.insertar_usuario(nuevo_usuario)

                # Actualiza la tabla
                self.modelo.tabla.append(nuevo_usuario)
                self.modelo.layoutChanged.emit()
                self.limpiarDatos()

    def on_boton_delete(self):
        indice = self.tvwTabla.selectedIndexes()
        if indice:
            if self.datos_crud.text_nombre.text() == "" or self.datos_crud.text_dni.text() == "" or self.datos_crud.cmb_xenero.currentIndex() == -1:
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
            if self.datos_crud.text_nombre.text() == "" or self.datos_crud.text_dni.text() == "" or self.datos_crud.cmb_xenero.currentIndex() == -1:
                print("Faltan datos para introducir")
            else:
                self.modelo.tabla[indice[0].row()][0] = self.datos_crud.text_nombre.text()
                self.modelo.tabla[indice[0].row()][1] = self.datos_crud.text_dni.text()
                self.modelo.tabla[indice[0].row()][2] = self.datos_crud.cmb_xenero.currentText()
                self.modelo.tabla[indice[0].row()][3] = True if self.datos_crud.boton_fallecido.isChecked() else False
                self.modelo.layoutChanged.emit()
                self.limpiarDatos()

    def limpiarDatos(self):
        self.datos_crud.text_nombre.clear()
        self.datos_crud.text_dni.clear()
        self.datos_crud.cmb_xenero.setCurrentIndex(-1)
        self.datos_crud.boton_fallecido.setChecked(False)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableView()
    app.exec()



'''
Hacer que al pulsar en una fila, se manden los datos a los campos de abajo
'''




