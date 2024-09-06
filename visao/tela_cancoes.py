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
from modelo.artista import Artista
from modelo.cancao import Cancao

from controle.controle_contexto import ControleContexto
from controle.artista_controle import ArtistaControle
from controle.cancao_controle import CancaoControle
from controle.playlist_controle import PlaylistControle

from visao.tela_criar_playlist import TelaCriarPlaylist

class CancaoItemList(QListWidgetItem):
    def __init__(self, cancao: Cancao) -> None:
        super().__init__(f'{cancao.titulo} - {cancao.artista} ({cancao.album})')
        self.cancao = cancao

class TelaCancoes(QWidget):
    def __init__(self,
                 fontes: Dict[str, QFont],
                 usuario: Usuario,
                 controle: ControleContexto,
                 func_tocar) -> None:

        super().__init__()

        self.controle = controle
        self.usuario = usuario
        self.func_tocar = func_tocar
        self.func_att_lista_play = None

        layout = QGridLayout(self)

        self.caixa_pesquisa = QLineEdit()
        self.caixa_pesquisa.setFixedSize(380, 30)
        self.caixa_pesquisa.setStyleSheet(
            "border-radius: 15px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.caixa_pesquisa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.caixa_pesquisa.setPlaceholderText("Digite o nome da canção :)")
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
        self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_cancao(self.caixa_pesquisa.text()))

        self.lista = QListWidget()
        self.lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        for cancao in self.usuario.colecao:
            itemlist = CancaoItemList(cancao)
            self.lista.addItem(itemlist)
        self.lista.installEventFilter(self)
        self.lista.itemDoubleClicked.connect(self.tocar_cancao)

        layout_pesquisa = QGridLayout()
        layout_pesquisa.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_pesquisa.addWidget(self.botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

        layout.setSpacing(10)
        layout.addLayout(layout_pesquisa, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lista, 1, 0)

    def eventFilter(self, watched: QObject, event: QEvent):
        if event.type() == QEvent.Type.ContextMenu and watched is self.lista:
            menu = QMenu()
            acao_apagar = menu.addAction("Apagar canção")
            acao_apagar.triggered.connect(self.remover_cancao)
            acao_tocar = menu.addAction("Tocar canção")
            acao_tocar.triggered.connect(self.tocar_cancao)
            acao_criar_playlist = menu.addAction("Criar playlist")
            acao_criar_playlist.triggered.connect(self.criar_playlist)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(watched, event)

    def remover_cancao(self):
        can_rem: CancaoItemList = self.lista.takeItem(
            self.lista.row(
                self.lista.selectedItems()[0]
                )
            )
        self.usuario.rem_cancao(can_rem.cancao)
        for playlist in self.usuario.playlists:
            playlist.rem_cancao(can_rem.cancao)

        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{can_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_cancao(self, texto: str):
        self.lista.clear()

        for cancao in self.usuario.colecao:
            itemlist = CancaoItemList(cancao)
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

    def tocar_cancao(self):
        can_tocar: CancaoItemList = self.lista.selectedItems()[0]
        self.func_tocar(can_tocar.cancao)
        self.lista.clearSelection()

    def exibir_playlist(self, playlist):
        self.lista.clear()
        for cancao in playlist.cancoes:
            itemlist = CancaoItemList(cancao)
            self.lista.addItem(itemlist)
    
    def criar_playlist(self):
        cancoes = [item.cancao for item in self.lista.selectedItems()]
        TelaCriarPlaylist(self.usuario, self, self.controle, cancoes, self.func_att_lista_play).show()

