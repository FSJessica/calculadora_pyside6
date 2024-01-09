import sys

from PySide6.QtGui   import QIcon
from display import Display
from main_window import  MainWindow
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from buttons import ButtonGrid
from variables import WINDOW_ICON_PATH

if __name__ =='__main__':
    #snake_case
    #PascalCase
    #camelCase

    #Cria a aplicação
    app= QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone:
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Display
    display = Display()
    display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    #Grid
    buttonsGrid = ButtonGrid(display)
    window.vlayout.addLayout(buttonsGrid)

    # buttonsGrid.addWidget(Button('0'), 0, 0)
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)
    # buttonsGrid.addWidget(Button('3'), 1, 0)


    #Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()