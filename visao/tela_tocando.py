from PySide6.QtCore import (
    Qt, QEvent, QObject
)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox, QLabel, QSlider
)
from PySide6.QtGui import (
    QFont, QPixmap
)

from typing import Dict

class TelaTocando(QWidget):

    def __init__(self,
                 fontes: Dict[str, QFont],
                 *args) -> None:
        
        super().__init__()

        self.setMinimumSize(args[0]/4, args[1] - 90)

        layout = QGridLayout(self)

        layout_topo = QGridLayout()

        self.titulo = QLabel("Nada esta tocando")
        self.titulo.setWordWrap(True)
        self.titulo.setFont(fontes["rotulo"])

        fonte_artista = fontes["rotulo"]
        fonte_artista.setPointSize(15)
        self.artista = QLabel("Nada esta tocando")
        self.artista.setWordWrap(True)
        self.artista.setFont(fonte_artista)
        self.artista.setStyleSheet("color: gray;")
        
        layout_topo.addWidget(self.titulo, 0, 0, Qt.AlignmentFlag.AlignLeft)
        layout_topo.addWidget(self.artista, 1, 0, Qt.AlignmentFlag.AlignLeft)

        self.img_capa = QLabel()
        self.img_capa.setFixedSize(300, 300)
        self.img_capa.setScaledContents(True)
        self.img_capa.setPixmap(QPixmap("visao/imgs/album_padrao.jpg"))

        self.botao_tocar = QPushButton("Play")
        self.botao_tocar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_tocar.setFixedSize(100,35)
        self.botao_tocar.setFont(fontes["botao"])
        self.botao_tocar.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 10px;")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setFixedSize(100, 20)

        layout_botoes = QGridLayout()
        layout_botoes.addWidget(self.botao_tocar, 0, 0, Qt.AlignmentFlag.AlignTop)

        layout.addLayout(layout_topo, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.img_capa, 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.slider, 2, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(layout_botoes, 2, 0, Qt.AlignmentFlag.AlignCenter)