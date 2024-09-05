from PySide6.QtCore import (
    Qt, QEvent, QObject, QSize
)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox, QLabel, QSlider
)
from PySide6.QtGui import (
    QFont, QPixmap, QIcon
)

from modelo.cancao import Cancao
from controle.controle_contexto import ControleContexto
from controle.album_controle import AlbumControle

from typing import Dict

class TelaTocando(QWidget):

    def __init__(self,
                 fontes: Dict[str, QFont],
                 controle: ControleContexto,
                 *args) -> None:
        
        super().__init__()

        self.setMinimumSize(args[0]/4, args[1] - 90)
        self.estado_botao_play = 1
        self.controle = controle

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

        self.botao_tocar = QPushButton()
        self.botao_tocar.setCursor(Qt.CursorShape.PointingHandCursor)
        img_play = QPixmap("visao/imgs/play.png")
        icon_play = QIcon(img_play)
        self.botao_tocar.setIcon(icon_play)
        self.botao_tocar.setIconSize(QSize(25, 25))
        self.botao_tocar.setFixedSize(100,35)
        self.botao_tocar.setFont(fontes["botao"])
        self.botao_tocar.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 15px;")
        self.botao_tocar.clicked.connect(self.clique_play)

        self.botao_anterior = QPushButton()
        self.botao_anterior.setCursor(Qt.CursorShape.PointingHandCursor)
        img_anterior = QPixmap("visao/imgs/anterior.png")
        icon_anterior = QIcon(img_anterior)
        self.botao_anterior.setIcon(icon_anterior)
        self.botao_anterior.setIconSize(QSize(25, 25))
        self.botao_anterior.setFixedSize(100,35)
        self.botao_anterior.setFont(fontes["botao"])
        self.botao_anterior.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 15px;")

        self.botao_proximo = QPushButton()
        self.botao_proximo.setCursor(Qt.CursorShape.PointingHandCursor)
        img_proximo = QPixmap("visao/imgs/proximo.png")
        icon_proximo = QIcon(img_proximo)
        self.botao_proximo.setIcon(icon_proximo)
        self.botao_proximo.setIconSize(QSize(25, 25))
        self.botao_proximo.setFixedSize(100,35)
        self.botao_proximo.setFont(fontes["botao"])
        self.botao_proximo.setStyleSheet("background-color: rgba(255,255,255,0.9); color: black; border-radius: 15px;")

        layout_botoes = QGridLayout()
        layout_botoes.addWidget(self.botao_anterior, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_botoes.addWidget(self.botao_tocar, 0, 1, Qt.AlignmentFlag.AlignTop)
        layout_botoes.addWidget(self.botao_proximo, 0, 2, Qt.AlignmentFlag.AlignTop)

        layout.addLayout(layout_topo, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.img_capa, 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(layout_botoes, 2, 0, Qt.AlignmentFlag.AlignCenter)
    
    def clique_play(self):
        if not self.estado_botao_play:
            img_play = QPixmap("visao/imgs/play.png")
            icon_play = QIcon(img_play)
            self.botao_tocar.setIcon(icon_play)
            self.estado_botao_play = 1
        else:
            img_pausa = QPixmap("visao/imgs/pausa.png")
            icon_pausa = QIcon(img_pausa)
            self.botao_tocar.setIcon(icon_pausa)
            self.estado_botao_play = 0
    
    def tocar_cancao(self, cancao: Cancao):
        self.titulo.setText(cancao.titulo)
        self.artista.setText(cancao.artista)
        self.controle.tipo_controle = AlbumControle()
        self.img_capa.setPixmap(QPixmap(self.controle.pesquisar("titulo", cancao.album)[0].img_capa))
        