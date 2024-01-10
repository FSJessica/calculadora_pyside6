
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #Configurado o layout básidco
        self.cw = QWidget()
        self.vlayout = QVBoxLayout()
        self.cw.setLayout(self.vlayout)
        self.setCentralWidget(self.cw)

        #Título da janela
        self.setWindowTitle('Calculadora')



    def adjustFixedSize(self):
        #ùltima coisa a ser feita
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.vlayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)