import sys

from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget,
                             QListView, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        super().__init__()
        self.setWindowTitle("TODO")
        self.setFixedSize(400, 400)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


#Todo: borrar, tenemos que detectar lo que este seleccionado para borrarlo


