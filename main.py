import sys

from PySide6.QtGui   import QIcon
from display import Display
from main_window import  MainWindow
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from buttons import ButtonsGrid
from variables import WINDOW_ICON_PATH
from info import Info

if __name__ =='__main__':

    #Cria a aplicação
    app= QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone:
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info ('Sua conta')
    window.addWidgetToVLayout(info)

    #Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    #Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vlayout.addLayout(buttonsGrid)


    #Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()