from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MessageBox(QMessageBox):
    def __init__(self, 
                 window_title: str,
                 icon: QIcon, 
                 *args) -> None:
        super().__init__()

        self.setIcon(icon)
        self.setWindowTitle(window_title)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.setText('\n'.join(args))