from PySide6.QtWidgets import QApplication
from visao.src.tela_login import TelaLogin

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    tela = TelaLogin()
    tela.show()
    
    app.exec()
