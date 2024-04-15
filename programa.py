from PySide6.QtWidgets import QApplication
from visao.src.tela_login import TelaLogin

import sys

class Programa:
    def __init__(self): pass

    def inicializar(self):
        app = QApplication(sys.argv)
        tela = TelaLogin()
        tela.show()
        app.exec()

Programa().inicializar()
