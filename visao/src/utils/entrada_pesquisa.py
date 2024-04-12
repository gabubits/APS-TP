from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLineEdit

class CaixaPesquisa(QLineEdit):
    def __init__(self):
        super().__init__()

        self.texto = ""
    def keyPressEvent(self, arg__1: QKeyEvent) -> None:
        print(arg__1.key())
        self.texto += arg__1.text()
        self.setText(self.texto)
