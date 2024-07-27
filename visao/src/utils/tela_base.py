from PySide6.QtGui import (
    QFontDatabase, QFont, QMouseEvent, QPixmap, QIcon,
    QScreen, QPainterPath, QPainter)

from PySide6.QtWidgets import (
    QWidget, QFrame, QSizePolicy, QLabel, QMainWindow,
    QPushButton, QHBoxLayout, QGridLayout, QLineEdit,
    QVBoxLayout, QApplication, QTextEdit, QFileDialog,
    QMessageBox, QListWidget, QListWidgetItem, QStackedWidget
    )

from PySide6.QtCore import (
    Qt, QSize, QPoint, qAbs)

from ..components.message_box import MessageBox
import pathlib
import os
import sys

class TelaBase(QMainWindow):
    def __init__(self, parent: QWidget | None,
                 titulo: str, tamanho: QSize) -> None:
        super().__init__(parent = parent)

        fonte_id = QFontDatabase.addApplicationFont(str(pathlib.Path("visao/src/fonts/SF-Pro.ttf").resolve()))
        if fonte_id < 0:
            raise Exception("Falha na importação da fonte")
        self.fonte_principal = QFontDatabase.applicationFontFamilies(fonte_id)[0]

        self.fonte_rotulo = QFont(self.fonte_principal, 10)
        self.fonte_rotulo.setWeight(QFont.Weight.Medium)

        self.fonte_entrada = QFont(self.fonte_principal, 10)
        self.fonte_entrada.setWeight(QFont.Weight.Normal)

        self.fonte_botao = QFont(self.fonte_principal, 15)
        self.fonte_botao.setWeight(QFont.Weight.DemiBold)

        self.setWindowTitle(titulo)
        self.setMinimumSize(tamanho)
        self.setStyleSheet("background-color: rgb(18, 18, 18);")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        self.centralizarTela()

        widget_central = QWidget()
        self.widget_central_layout = QGridLayout(widget_central)
        self.setCentralWidget(widget_central)

        self.oldPos = self.pos()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = QPoint(event.position().x(),event.position().y())
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:

            self.move(self.pos() + QPoint(event.scenePosition().x(),event.scenePosition().y()) - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
    
    def centralizarTela(self) -> None:
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
