from PySide6.QtCore import Qt, QEvent, QObject
from PySide6.QtWidgets import (
    QWidget, QListWidget, QGridLayout, QLineEdit, QPushButton, QMenu, QListWidgetItem,
    QMessageBox, QVBoxLayout
)
from PySide6.QtGui import QFont, QContextMenuEvent

from typing import Dict
from controle.usuario_controle import UsuarioControle
from modelo.playlist import Playlist
from modelo.usuario import Usuario
from controle.controle_contexto import ControleContexto
from controle.playlist_controle import PlaylistControle

class PlaylistItemList(QListWidgetItem):
    def __init__(self, playlist: Playlist) -> None:
        super().__init__(f'{playlist.nome} - {playlist.descricao}')
        self.playlist = playlist

class TelaPlaylists(QWidget):
    def __init__(self, fontes: Dict[str, QFont], usuario: Usuario, controle: ControleContexto) -> None:
        super().__init__()

        self.controle = controle
        self.usuario_controle = UsuarioControle()
        self.usuario = usuario

        layout = QGridLayout(self)

        # Configuração da Caixa de Pesquisa
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

        # Conectar o sinal textChanged à função de pesquisa
        self.caixa_pesquisa.textChanged.connect(lambda: self.pesquisar_playlist(self.caixa_pesquisa.text()))

        # Botão de Pesquisa
        self.botao_pesquisar = QPushButton("Pesquisar")
        self.botao_pesquisar.setFixedSize(200, 30)
        self.botao_pesquisar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.botao_pesquisar.setFont(fontes["botao"])
        self.botao_pesquisar.setStyleSheet(
            "background-color: rgba(255,255,255,0.9);" +
            "color: black;" +
            "border-radius: 15px;"
        )
        # Conectar o botão de pesquisa à função de pesquisa
        self.botao_pesquisar.clicked.connect(lambda: self.pesquisar_playlist(self.caixa_pesquisa.text()))

        # Configuração da Lista
        self.lista = QListWidget()
        self.lista.setStyleSheet(
            "border-radius: 5px;" +
            "background-color: rgb(18, 18, 18);" +
            "border: 1px solid grey"
        )
        self.lista.setFont(fontes["lista"])
        self.lista.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.controle.tipo_controle = PlaylistControle()
        
        # Adicionar playlists à lista
        self.carregar_playlists()
        
        # Instalar o filtro de evento para o menu de contexto
        self.lista.installEventFilter(self)

        # Layouts
        layout_pesquisa = QGridLayout()
        layout_pesquisa.addWidget(self.caixa_pesquisa, 0, 0, Qt.AlignmentFlag.AlignTop)
        layout_pesquisa.addWidget(self.botao_pesquisar, 0, 1, Qt.AlignmentFlag.AlignTop)

        layout.setSpacing(10)
        layout.addLayout(layout_pesquisa, 0, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lista, 1, 0)

    def carregar_playlists(self):
        """Carrega todas as playlists na lista."""
        self.lista.clear()
        for play in self.usuario.playlists:
            itemlist = PlaylistItemList(play)
            self.lista.addItem(itemlist)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if isinstance(event, QContextMenuEvent) and watched is self.lista:
            if self.lista.selectedItems():
                menu = QMenu()
                acao_apagar = menu.addAction("Apagar playlist")
                acao_apagar.triggered.connect(self.remover_playlist)

                menu.exec_(event.globalPos())
            return True
        
        return super().eventFilter(watched, event)

    def remover_playlist(self):
        if not self.lista.selectedItems():
            return
        
        item_selecionado = self.lista.selectedItems()[0]
        row = self.lista.row(item_selecionado)
        play_rem: PlaylistItemList = self.lista.takeItem(row)
        self.controle.tipo_controle = PlaylistControle()
        self.usuario_controle.remover_playlist(self.usuario, play_rem.playlist)
        self.controle.remover(play_rem.playlist)
        
        msg_sucesso = QMessageBox(self)
        msg_sucesso.setIcon(QMessageBox.Icon.Information)
        msg_sucesso.setWindowTitle("Removido com sucesso!")
        msg_sucesso.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_sucesso.setText(f"{play_rem.text()} foi removido com sucesso!")
        msg_sucesso.exec()

    def pesquisar_playlist(self, texto: str):
        """Filtra a lista de playlists com base no texto de entrada."""
        texto = texto.lower().strip()
        for index in range(self.lista.count()):
            item = self.lista.item(index)
            item_text = item.text().lower()
            item.setHidden(texto not in item_text)
