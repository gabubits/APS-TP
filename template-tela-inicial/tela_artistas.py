# Tela de artistas
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton
)
from PySide6.QtGui import (
    QFont
)
from typing import Dict

class Artista:
    def __init__(self) -> None:
        self.nome = None
        self.bio = None
        self.img_perfil = None
        self.nacionalidade = None
        self.comentario = None
        self.artista_id = None
        self.albuns = []

class TelaArtistas(QWidget):

    def __init__(self,
                 fontes: Dict[str, QFont]) -> None:
        super().__init__()
        layout = QGridLayout(self)

        caixa_pesquisa = QLineEdit()
        caixa_pesquisa.setFixedSize(380, 30)
        caixa_pesquisa.setStyleSheet(
            "border-radius: 15px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        caixa_pesquisa.setPlaceholderText("Digite o nome do artista :)")
        caixa_pesquisa.setFont(fontes["entrada"])

        botao_pesquisar = QPushButton("Pesquisar")
        botao_pesquisar.setFixedSize(200, 30)
        botao_pesquisar.setCursor(Qt.CursorShape.PointingHandCursor)
        botao_pesquisar.setFont(fontes["botao"])
        botao_pesquisar.setStyleSheet(
            "background-color: rgba(255,255,255,0.9);" +
            "color: black;" +
            "border-radius: 15px;"
        )

        lista = QListWidget()
        lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        print(fontes["lista"])
        lista.setFont(fontes["lista"])
        lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        lista.addItems(['Sevdaliza', 'Kelela', 'Cecile Believe'])

        layout_pesquisa = QGridLayout()
        layout_pesquisa.addWidget(caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_pesquisa.addWidget(botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

        layout.setSpacing(10)
        layout.addLayout(layout_pesquisa, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lista, 1, 0)

