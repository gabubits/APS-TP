from PySide6.QtCore import (
    Qt, QEvent, QObject
)
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout,
    QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox, QTableWidget, QHeaderView, QHBoxLayout,
    QTableWidgetItem
)
from PySide6.QtGui import (
    QFont
)

from typing import Dict
from modelo.usuario import Usuario
from modelo.album import Album

from controle.controle_contexto import ControleContexto
from controle.album_controle import AlbumControle
from controle.artista_controle import ArtistaControle
from controle.cancao_controle import CancaoControle
from controle.playlist_controle import PlaylistControle

class AlbumItemList(QListWidgetItem):
    def __init__(self, album_id, album_titulo, album_artistas) -> None:
        super().__init__(f'{album_titulo} - {album_artistas}')
        self.alb_id = str(album_id)

class TelaAlbuns(QWidget):
    def __init__(self,
                 fontes: Dict[str, QFont],
                 usuario: Usuario,
                 controle: ControleContexto) -> None:
        
        super().__init__()

        self.controle = controle
        self.usuario = usuario

        layout = QGridLayout(self)

        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setFixedSize(380, 30)
        self.caixa_pesquisa.setStyleSheet(
            "border-radius: 15px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caixa_pesquisa.setPlaceholderText("Digite o nome do álbum :)")
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
        self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_album(self.caixa_pesquisa.text()))

        self.lista = QListWidget()
        self.lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        for cancao_id in self.usuario.cancoes:
            self.controle.tipo_controle = CancaoControle()
            album_id = self.controle.pesquisar("id", str(cancao_id))[0].album
            self.controle.tipo_controle = AlbumControle()
            album = self.controle.pesquisar("id", str(album_id))
            self.controle.tipo_controle = ArtistaControle()
            album_artistas = ", ".join([self.controle.pesquisar("id", str(artista_id))[0].nome for artista_id in album.artistas])
            itemlist = AlbumItemList(album.id, album.titulo, album_artistas)
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
            acao_apagar = menu.addAction("Apagar álbum")
            acao_apagar.triggered.connect(self.remover_album)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(watched, event)
    
    def remover_album(self):
        alb_rem: AlbumItemList = self.lista.takeItem(
            self.lista.row(
                self.lista.selectedItems()[0]
                )
            )
        
        self.controle.tipo_controle = AlbumControle()
        cancoes_id = self.controle.pesquisar("id", alb_rem.alb_id)[0].cancoes
        self.usuario.cancoes = [cancao_id for cancao_id in self.usuario.cancoes if cancao_id not in cancoes_id]
        self.controle.tipo_controle = PlaylistControle()
        for playlist_id in self.usuario.playlists:
            playlist = self.controle.pesquisar("id", str(playlist_id))[0]
            playlist.cancoes = [cancao_id for cancao_id in playlist.cancoes if cancao_id not in cancoes_id]

        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{alb_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_album(self, texto: str):
        self.lista.clear()
        
        for cancao_id in self.usuario.cancoes:
            self.controle.tipo_controle = CancaoControle()
            album_id = self.controle.pesquisar("id", str(cancao_id))[0].album
            self.controle.tipo_controle = AlbumControle()
            album = self.controle.pesquisar("id", str(album_id))
            self.controle.tipo_controle = ArtistaControle()
            album_artistas = ", ".join([self.controle.pesquisar("id", str(artista_id))[0].nome for artista_id in album.artistas])
            itemlist = AlbumItemList(album.id, album.titulo, album_artistas)
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