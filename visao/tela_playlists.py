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

from controle.controle_contexto import ControleContexto
from controle.playlist_controle import PlaylistControle

class PlaylistItemList(QListWidgetItem):
    def __init__(self, playlist_id, playlist_nome, playlist_descricao) -> None:
        super().__init__(f'{playlist_nome} - {playlist_descricao}')
        self.play_id = str(playlist_id)

class TelaPlaylists(QWidget):
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
        self.caixa_pesquisa.setPlaceholderText("Digite o nome da playlist :)")
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
        self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_playlist(self.caixa_pesquisa.text()))

        self.lista = QListWidget()
        self.lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.controle.tipo_controle = PlaylistControle()
        for playlist_id in self.usuario.playlists:
            playlist = self.controle.pesquisar("id", str(playlist_id))[0]
            itemlist = PlaylistItemList(playlist_id, playlist.nome, playlist.descricao)
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
            acao_apagar = menu.addAction("Apagar playlist")
            acao_apagar.triggered.connect(self.remover_playlist)

            menu.exec_(event.globalPos())
            return True
        return super().eventFilter(watched, event)
    
    def remover_playlist(self):
        play_rem: PlaylistItemList = self.lista.takeItem(
            self.lista.row(
                self.lista.selectedItems()[0]
                )
            )
        
        self.usuario.rem_playlist(play_rem.play_id)
        self.controle.tipo_controle = PlaylistControle()
        self.controle.remover(play_rem.play_id)

        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{play_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_playlist(self, texto: str):
        self.lista.clear()
        
        for playlist_id in self.usuario.playlists:
            playlist = self.controle.pesquisar("id", str(playlist_id))[0]
            itemlist = PlaylistItemList(playlist_id, playlist.nome, playlist.descricao)
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