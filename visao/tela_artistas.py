from PySide6.QtCore import (
    Qt, QEvent, QObject
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
from modelo.usuario import Usuario
from modelo.artista import Artista

from controle.controle_contexto import ControleContexto
from controle.album_controle import AlbumControle
from controle.artista_controle import ArtistaControle
from controle.cancao_controle import CancaoControle
from controle.playlist_controle import PlaylistControle

class ArtistaItemList(QListWidgetItem):
    def __init__(self, artista: Artista) -> None:
        super().__init__(artista.nome)
        self.artista = artista

class TelaArtistas(QWidget):

    def __init__(self,
                 fontes: Dict[str, QFont],
                 usuario: Usuario,
                 controle: ControleContexto) -> None:
        
        super().__init__()
        layout = QGridLayout(self)

        self.controle = controle
        self.usuario = usuario

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
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        for cancao in self.usuario.cancoes:
            self.controle.tipo_controle = ArtistaControle()
            artista = self.controle.pesquisar("nome", str(cancao.artista))[0]
            itemlist = ArtistaItemList(artista)
            if not self.lista.findItems(itemlist.text(), Qt.MatchFlag.MatchExactly):
                self.lista.addItem(itemlist)
        self.lista.installEventFilter(self)

        layout_pesquisa = QGridLayout()
        layout_pesquisa.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_pesquisa.addWidget(self.botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

        layout.setSpacing(10)
        layout.addLayout(layout_pesquisa, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lista, 1, 0)
    
    def eventFilter(self, watched: QObject, event: QEvent):
        if event.type() == QEvent.Type.ContextMenu and watched is self.lista:
            menu = QMenu()
            acao_apagar = menu.addAction("Apagar artista")
            acao_apagar.triggered.connect(self.remover_artista)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(watched, event)
    
    def remover_artista(self):
        art_rem: ArtistaItemList = self.lista.takeItem(
            self.lista.row(
                self.lista.selectedItems()[0]
                )
            )
        
        for i in range(len(self.usuario.colecao)):
            if self.usuario.colecao[i].artista == art_rem.artista.nome:
                self.usuario.rem_cancao(self.usuario.colecao[i])

        for playlist in self.usuario.playlists:
            for i in range(len(playlist.cancoes)):
                if playlist.cancoes[i].artista == art_rem.artista.nome:
                    playlist.rem_cancao(playlist.cancoes[i])
        
        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{art_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_artista(self, texto: str):
        self.lista.clear()

        for cancao in self.usuario.cancoes:
            self.controle.tipo_controle = ArtistaControle()
            artista = self.controle.pesquisar("nome", str(cancao.artista))[0]
            itemlist = ArtistaItemList(artista)
            if not self.lista.findItems(itemlist.text(), Qt.MatchFlag.MatchExactly):
                self.lista.addItem(itemlist)
        
        if len(texto.rstrip()) == 0:
            for index in range(self.lista.count()): 
                self.lista.item(index).setHidden(False)
            return
        for index in range(self.lista.count()):
            item = self.lista.item(index)
            if texto.rstrip() not in item.text(): 
                item.setHidden(True)
            else: item.setHidden(False)
    
