from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

class MessageBox(QMessageBox):
    def __init__(self,
                 parent,
                 window_title: str,
                 icon: QIcon, 
                 *args) -> None:
        super().__init__(parent = parent)

        self.setIcon(icon)
        self.setWindowTitle(window_title)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        text = ""
        for arg in args:
            if type(arg) == list:
                text += '\n'.join(arg)
            else: text += arg + '\n'
        self.setText(text)