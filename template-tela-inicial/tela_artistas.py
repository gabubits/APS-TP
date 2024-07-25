# Tela de artistas
from PySide6.QtCore import (
    Qt, QEvent,
)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox
)
from PySide6.QtGui import (
    QFont
)
from typing import Dict

class Artista:
    def __init__(self, nome = None, id = -1) -> None:
        self.nome = nome
        self.bio = ''
        self.img_perfil = ''
        self.nacionalidade = 'Brasileira'
        self.comentario = 'Digite seu comentario'
        self.artista_id = id
        self.albuns = []
    
    def add_album(self, album):
        self.albuns.append(album)
    
    def rem_album(self, album):
        self.albuns.remove(album)

    def to_dict(self):
        return {
            'nome': self.nome,
            'bio': self.bio,
            'img_perfil': self.img_perfil,
            'nacionalidade': self.nacionalidade,
            'comentario': self.comentario,
            'artista_id': self.artista_id,
            'albuns': []
            # 'albuns': [album.to_dict() for album in self.albuns]
        }
    
    def __repr__(self) -> str:
        return f'{self.nome}'

    def __str__(self) -> str:
        return f'{self.nome} - {self.nacionalidade} ({len(self.albuns)} álbuns)'

class ArtistaItemList(QListWidgetItem):
    def __init__(self, artista: Artista) -> None:
        super().__init__(artista.nome)
        self.id = artista.artista_id
class TelaArtistas(QWidget):

    def __init__(self,
                 fontes: Dict[str, QFont]) -> None:
        super().__init__()
        layout = QGridLayout(self)

        self.artistas = [Artista(f'Artista {i}', i) for i in range(3)]

        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setFixedSize(380, 30)
        self.caixa_pesquisa.setStyleSheet(
            "border-radius: 15px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caixa_pesquisa.setPlaceholderText("Digite o nome do artista :)")
        self.caixa_pesquisa.setFont(fontes["entrada"])

        self.botao_pesquisar = QPushButton("Pesquisar")
        self.botao_pesquisar.setFixedSize(200, 30)
        self.botao_pesquisar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_pesquisar.setFont(fontes["botao"])
        self.botao_pesquisar.setStyleSheet(
            "background-color: rgba(255,255,255,0.9);" +
            "color: black;" +
            "border-radius: 15px;"
        )
        self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_artista(self.caixa_pesquisa.text()))

        self.lista = QListWidget()
        self.lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        print(fontes["lista"])
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        for artista in self.artistas:
            self.lista.addItem(ArtistaItemList(artista))
        self.lista.installEventFilter(self)

        layout_pesquisa = QGridLayout()
        layout_pesquisa.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_pesquisa.addWidget(self.botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

        layout.setSpacing(10)
        layout.addLayout(layout_pesquisa, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lista, 1, 0)
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.ContextMenu and source is self.lista:
            menu = QMenu()
            acao_apagar = menu.addAction("Apagar artista")
            acao_apagar.triggered.connect(self.remover_artista)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(source, event)
    
    def remover_artista(self):
        art_rem = self.lista.takeItem(self.lista.row(self.lista.selectedItems()[0]))
        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{art_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_artista(self, texto: str):
        print(self.lista.count())
        if len(texto.rstrip()) == 0:
            for index in range(self.lista.count()): 
                self.lista.item(index).setHidden(False)
            return
        for index in range(self.lista.count()):
            item = self.lista.item(index)
            if texto.rstrip() not in item.text(): 
                item.setHidden(True)
            else: item.setHidden(False)



