from PySide6.QtWidgets import *
from visao.src.tela_login import TelaLogin
from persistencia.usuario_p import UsuarioP

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tela = TelaLogin()
    tela.show()
    
    app.exec()
