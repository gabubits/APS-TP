from PySide6.QtWidgets import QApplication
from visao.tela_login import TelaLogin

import sys

class Programa:
    @staticmethod
    def inicializar():
        app = QApplication(sys.argv)
        tela = TelaLogin()
        tela.show()
        app.exec()

Programa.inicializar()
